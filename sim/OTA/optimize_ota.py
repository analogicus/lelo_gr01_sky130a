#!/usr/bin/env python3
"""
OTA Optimization Script
Automatically adjusts transistor sizing and runs simulations to optimize
gain, unity-gain frequency, and phase margin.

Optimizes only the active OTA circuitry (two-stage Miller OTA):
- Stage 1: Differential pair with active loads
- Stage 2: Output stage with class-A driver
Does NOT modify the bias current generator.

Uses Bayesian-like optimization with exploration/exploitation balance.
"""

import re
import subprocess
import os
import json
import random
import math
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
import copy

# ============================================================================
# Configuration
# ============================================================================

SCHEMATIC_PATH = "../../design/LELO_GR01_SKY130A/OTA.sch"
WORK_DIR = "../../work"
SIM_DIR = "."

# Target specifications
TARGETS = {
    "gain_db": 80.0,      # Target gain in dB
    "ugf": 10e6,         # Target UGF in Hz (10 MHz)
    "phase_margin": 60.0, # Minimum phase margin in degrees
    "vb2_min": 0.45,      # Minimum VB2 bias voltage
    "vb2_max": 0.65,      # Maximum VB2 bias voltage
}

# Optimization parameters
MAX_ITERATIONS = 10000
CONVERGENCE_THRESHOLD = 0.5   # Stop if improvement < 0.5%
EXPLORATION_RATE = 0.25       # Probability of random exploration
ITERATIONS_BEFORE_COOLING = 1000

# ============================================================================
# Data Classes
# ============================================================================

@dataclass
class TransistorSizing:
    """Represents the sizing parameters for the active OTA (two-stage Miller)
    
    NOTE: This only includes transistors in the active OTA circuitry.
    The bias current generator is NOT included and will not be modified.
    
    Stage 1 - Differential Input with Active Loads:
        - x11/x12: Input differential pair (JNWATR_NCH)
        - x15/x14: Active load current mirrors (JNWATR_PCH)
        - x13: Tail current source (JNWATR_NCH)
    
    Stage 2 - Output Stage:
        - x2: Output stage PMOS (current source)
        - x1: Output stage NMOS (class-A driver)
    """
    # Stage 1 - Input differential pair
    diff_pair_1_count: int = 2     # x11 - Input NMOS (left) at -860 -170
    diff_pair_2_count: int = 2     # x12 - Input NMOS (right) at -580 -170
    
    # Stage 1 - Active loads (JNWATR_PCH)
    active_load_1_count: int = 2   # x15 - PCH at -780 -310
    active_load_2_count: int = 2   # x14 - PCH at -660 -310
    
    # Stage 1 - Tail current source
    current_source_2_count: int = 2  # x13 - NCH at -760 10
    
    # Stage 2 - Output stage PMOS
    stage_2_pmos_count: int = 2      # x2 - PCH at -400 -240
    
    # Stage 2 - Output stage NMOS (class-A)
    class_a_1_count: int = 4         # x1 - NCH at -400 10
    
    def to_dict(self) -> Dict:
        return {
            "diff_pair_1": self.diff_pair_1_count,
            "diff_pair_2": self.diff_pair_2_count,
            "active_load_1": self.active_load_1_count,
            "active_load_2": self.active_load_2_count,
            "current_source_2": self.current_source_2_count,
            "stage_2_pmos": self.stage_2_pmos_count,
            "class_a_1": self.class_a_1_count,
        }
    
    def copy(self) -> 'TransistorSizing':
        return copy.deepcopy(self)


@dataclass 
class SimulationResult:
    """Results from a single simulation run"""
    gain_db: float = 0.0
    ugf: float = 0.0
    phase_margin: float = 0.0
    vb1: float = 0.0
    vb2: float = 0.0
    success: bool = False
    error_msg: str = ""
    
    def score(self, targets: Dict) -> float:
        """Calculate a weighted score (higher is better)"""
        if not self.success:
            return -1000.0
        
        score = 0.0
        
        # UGF score (0-60 points) - weighted heavily  
        ugf_ratio = min(self.ugf / targets["ugf"], 1.0)
        if ugf_ratio >= 1.0:
            score += 40 + 5 * min(ugf_ratio - 1.0, 0.5)  # Bonus for exceeding target
        else:
            score += 40 * ugf_ratio
        
        # Gain score (0-20 points) - weighted heavily
        if ugf_ratio < 0.8: 
            gain_ratio = min(self.gain_db / targets["gain_db"], 1.0)
        else:
            gain_ratio = self.gain_db / targets["gain_db"]
        score += 40 * gain_ratio
        
        # Phase margin score (0-10 points)
        if self.phase_margin >= targets["phase_margin"]:
            score += 5
        else:
            score += 5 * (self.phase_margin / targets["phase_margin"])
        
        return score


@dataclass
class OptimizationState:
    """Tracks the optimization history and best results"""
    history: List[Tuple[TransistorSizing, SimulationResult]] = field(default_factory=list)
    best_sizing: Optional[TransistorSizing] = None
    best_result: Optional[SimulationResult] = None
    best_score: float = -float('inf')
    iteration: int = 0


# ============================================================================
# Schematic Modification Functions
# ============================================================================

def read_schematic(path: str) -> str:
    """Read the schematic file"""
    with open(path, 'r') as f:
        return f.read()


def write_schematic(path: str, content: str):
    """Write the schematic file"""
    with open(path, 'w') as f:
        f.write(content)


def format_instance_name(base_name: str, count: int) -> str:
    """Format instance name with proper bus notation"""
    if count == 1:
        return base_name
    else:
        return f"{base_name}[{count-1}:0]"


def parse_instance_count(line: str, name_pattern: str) -> int:
    """Parse the instance count from a schematic line.
    Returns 1 for single instance (name=x1), or N+1 for array (name=x1[N:0])
    """
    # Match array notation like name=x1[19:0]
    match = re.search(rf'name={name_pattern}\[(\d+):0\]', line)
    if match:
        return int(match.group(1)) + 1
    # Match single instance like name=x1 (followed by space or end)
    match = re.search(rf'name={name_pattern}(?:\s|$|\}})', line)
    if match:
        return 1
    return 0


def parse_sizing_from_schematic(schematic: str) -> TransistorSizing:
    """Parse current transistor sizing from schematic content.
    
    Only parses the active OTA components, not the bias generator.
    """
    sizing = TransistorSizing()
    
    for line in schematic.split('\n'):
        # Stage 1 - Input differential pair NMOS
        # x11 at -860 -170
        if 'name=x11' in line and 'JNWATR_NCH' in line and '-860 -170' in line:
            count = parse_instance_count(line, 'x11')
            if count > 0:
                sizing.diff_pair_1_count = count
        
        # x12 at -580 -170
        elif 'name=x12' in line and 'JNWATR_NCH' in line and '-580 -170' in line:
            count = parse_instance_count(line, 'x12')
            if count > 0:
                sizing.diff_pair_2_count = count
        
        # Stage 1 - Active load PMOS
        # x15 at -780 -310
        elif 'name=x15' in line and 'JNWATR_PCH' in line and '-780 -310' in line:
            count = parse_instance_count(line, 'x15')
            if count > 0:
                sizing.active_load_1_count = count
        
        # x14 at -660 -310
        elif 'name=x14' in line and 'JNWATR_PCH' in line and '-660 -310' in line:
            count = parse_instance_count(line, 'x14')
            if count > 0:
                sizing.active_load_2_count = count
        
        # Stage 1 - Tail current source
        # x13 at -760 10
        elif 'name=x13' in line and 'JNWATR_NCH' in line and '-760 10' in line:
            count = parse_instance_count(line, 'x13')
            if count > 0:
                sizing.current_source_2_count = count
        
        # Stage 2 - Output stage PMOS
        # x2 at -400 -240
        elif 'name=x2' in line and 'JNWATR_PCH' in line and '-400 -240' in line:
            count = parse_instance_count(line, 'x2')
            if count > 0:
                sizing.stage_2_pmos_count = count
        
        # Stage 2 - Output stage NMOS (class-A)
        # x1 at -400 10
        elif 'name=x1' in line and 'JNWATR_NCH' in line and '-400 10' in line:
            count = parse_instance_count(line, 'x1')
            if count > 0:
                sizing.class_a_1_count = count
    
    return sizing


def apply_sizing(schematic: str, sizing: TransistorSizing) -> str:
    """Apply transistor sizing to schematic content.
    
    Only modifies the active OTA components, not the bias generator.
    """
    lines = schematic.split('\n')
    result_lines = []
    
    for line in lines:
        modified_line = line
        
        # Stage 1 - Input differential pair NMOS
        # x11 at -860 -170
        if 'name=x11' in line and 'JNWATR_NCH' in line and '-860 -170' in line:
            if sizing.diff_pair_1_count == 1:
                modified_line = re.sub(r'name=x11\[\d+:\d+\]', 'name=x11', line)
                modified_line = re.sub(r'name=x11\s+', 'name=x11 ', modified_line)
            else:
                modified_line = re.sub(r'name=x11(\[\d+:\d+\])?\s*', f'name=x11[{sizing.diff_pair_1_count-1}:0] ', line)
        
        # x12 at -580 -170
        elif 'name=x12' in line and 'JNWATR_NCH' in line and '-580 -170' in line:
            if sizing.diff_pair_2_count == 1:
                modified_line = re.sub(r'name=x12\[\d+:\d+\]', 'name=x12', line)
                modified_line = re.sub(r'name=x12\s+', 'name=x12 ', modified_line)
            else:
                modified_line = re.sub(r'name=x12(\[\d+:\d+\])?\s*', f'name=x12[{sizing.diff_pair_2_count-1}:0] ', line)
        
        # Stage 1 - Active load PMOS
        # x15 at -780 -310
        elif 'name=x15' in line and 'JNWATR_PCH' in line and '-780 -310' in line:
            if sizing.active_load_1_count == 1:
                modified_line = re.sub(r'name=x15\[\d+:\d+\]', 'name=x15', line)
            else:
                modified_line = re.sub(r'name=x15(\[\d+:\d+\])?\s*', f'name=x15[{sizing.active_load_1_count-1}:0] ', line)
        
        # x14 at -660 -310
        elif 'name=x14' in line and 'JNWATR_PCH' in line and '-660 -310' in line:
            if sizing.active_load_2_count == 1:
                modified_line = re.sub(r'name=x14\[\d+:\d+\]', 'name=x14', line)
            else:
                modified_line = re.sub(r'name=x14(\[\d+:\d+\])?\s*', f'name=x14[{sizing.active_load_2_count-1}:0] ', line)
        
        # Stage 1 - Tail current source
        # x13 at -760 10
        elif 'name=x13' in line and 'JNWATR_NCH' in line and '-760 10' in line:
            if sizing.current_source_2_count == 1:
                modified_line = re.sub(r'name=x13\[\d+:\d+\]', 'name=x13', line)
            else:
                modified_line = re.sub(r'name=x13(\[\d+:\d+\])?\s*', f'name=x13[{sizing.current_source_2_count-1}:0] ', line)
        
        # Stage 2 - Output stage PMOS
        # x2 at -400 -240
        elif 'name=x2' in line and 'JNWATR_PCH' in line and '-400 -240' in line:
            if sizing.stage_2_pmos_count == 1:
                modified_line = re.sub(r'name=x2\[\d+:\d+\]', 'name=x2', line)
            else:
                modified_line = re.sub(r'name=x2(\[\d+:\d+\])?\s*', f'name=x2[{sizing.stage_2_pmos_count-1}:0] ', line)
        
        # Stage 2 - Output stage NMOS (class-A)
        # x1 at -400 10
        elif 'name=x1' in line and 'JNWATR_NCH' in line and '-400 10' in line:
            if sizing.class_a_1_count == 1:
                modified_line = re.sub(r'name=x1\[\d+:\d+\]', 'name=x1', line)
            else:
                modified_line = re.sub(r'name=x1(\[\d+:\d+\])?\s*', f'name=x1[{sizing.class_a_1_count-1}:0] ', line)
        
        result_lines.append(modified_line)
    
    return '\n'.join(result_lines)
# ============================================================================
# Simulation Functions
# ============================================================================

def run_simulation() -> SimulationResult:
    """Run netlist generation and AC simulation, return results"""
    result = SimulationResult()
    
    try:
        # Generate netlist
        netlist_cmd = f"cd {WORK_DIR} && make xsch CELL=OTA 2>&1"
        proc = subprocess.run(netlist_cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        if proc.returncode != 0:
            result.error_msg = f"Netlist generation failed: {proc.stderr}"
            return result
        
        # Run AC simulation with timeout command to ensure proper process termination
        # Using timeout --kill-after to forcefully kill if it doesn't respond to SIGTERM
        sim_cmd = f"cd {SIM_DIR} && timeout --kill-after=10s 90s make ac 2>&1"
        proc = subprocess.run(sim_cmd, shell=True, capture_output=True, text=True, timeout=120)
        
        # The simulation may return non-zero due to cicsim post-processing errors,
        # but the actual simulation results are written to output files.
        # Read results from the YAML output file
        yaml_path = os.path.join(SIM_DIR, "output_ac", "ac_SchGtKttTtVt.yaml")
        if os.path.exists(yaml_path):
            with open(yaml_path, 'r') as f:
                yaml_content = f.read()
            
            # Parse gain_db
            gain_match = re.search(r'^gain_db:\s*([\d.]+)', yaml_content, re.MULTILINE)
            if gain_match:
                result.gain_db = float(gain_match.group(1))
            
            # Parse UGF (must match at start of line to avoid phase_ugf)
            ugf_match = re.search(r'^ugf:\s*([\d.eE+-]+)', yaml_content, re.MULTILINE)
            if ugf_match:
                result.ugf = float(ugf_match.group(1))
            
            # Parse phase margin
            pm_match = re.search(r'^phase_margin:\s*([\d.]+)', yaml_content, re.MULTILINE)
            if pm_match:
                result.phase_margin = float(pm_match.group(1))
        
        # Also try to read VB1/VB2 from the simulation log file
        log_path = os.path.join(SIM_DIR, "output_ac", "ac_SchGtKttTtVt.log")
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                log_content = f.read()
            
            vb1_match = re.search(r'xdut\.vb1\s*=\s*([\d.eE+-]+)', log_content)
            if vb1_match:
                result.vb1 = float(vb1_match.group(1))
                
            vb2_match = re.search(r'xdut\.vb2\s*=\s*([\d.eE+-]+)', log_content)
            if vb2_match:
                result.vb2 = float(vb2_match.group(1))
        
        # Check if simulation was killed by timeout (exit code 124 or 137)
        if proc.returncode == 124 or proc.returncode == 137:
            result.error_msg = "Simulation timed out (ngspice convergence issue)"
            return result
        
        # Check if we got valid results
        if result.gain_db > 0 and result.ugf > 0:
            result.success = True
        else:
            result.error_msg = "Could not parse simulation results from output files"
            
    except subprocess.TimeoutExpired:
        result.error_msg = "Simulation timed out"
    except Exception as e:
        result.error_msg = str(e)
    
    return result


# ============================================================================
# Optimization Algorithm
# ============================================================================

def get_neighbor(sizing: TransistorSizing, exploration: bool = False) -> TransistorSizing:
    """Generate a neighboring sizing configuration.
    
    Only optimizes the active OTA components, not the bias generator.
    """
    new_sizing = sizing.copy()
    
    # Define parameter ranges for active OTA components only
    # Bias current generator components are NOT included
    param_ranges = {
        # Stage 1 - Input differential pair
        'diff_pair_1_count': (1, 8),
        'diff_pair_2_count': (1, 8),
        # Stage 1 - Active loads
        'active_load_1_count': (1, 8),
        'active_load_2_count': (1, 8),
        # Stage 1 - Tail current source
        'current_source_2_count': (1, 8),
        # Stage 2 - Output stage
        'stage_2_pmos_count': (1, 8),
        'class_a_1_count': (1, 8),
    }
    
    if exploration:
        # Random exploration - pick random values
        param = random.choice(list(param_ranges.keys()))
        min_val, max_val = param_ranges[param]
        setattr(new_sizing, param, random.randint(min_val, max_val))
    else:
        # Local search - small step in random direction
        param = random.choice(list(param_ranges.keys()))
        current_val = getattr(new_sizing, param)
        min_val, max_val = param_ranges[param]
        
        # Step size based on parameter
        step = random.choice([-2, -1, 1, 2])
        new_val = max(min_val, min(max_val, current_val + step))
        setattr(new_sizing, param, new_val)
    
    # Keep diff_pair_1 and diff_pair_2 matched (input pair must be matched)
    new_sizing.diff_pair_2_count = new_sizing.diff_pair_1_count
    
    # Keep active_load_1 and active_load_2 matched (current mirror must be matched)
    new_sizing.active_load_2_count = new_sizing.active_load_1_count
    
    return new_sizing


def simulated_annealing_step(
    state: OptimizationState,
    current_sizing: TransistorSizing,
    current_score: float,
    temperature: float,
    consecutive_failures: int = 0
) -> Tuple[TransistorSizing, float, bool, int]:
    """
    Perform one step of simulated annealing optimization.
    Returns (new_sizing, new_score, accepted, new_consecutive_failures)
    """
    # Increase exploration rate when stuck or after failures
    effective_exploration = EXPLORATION_RATE
    if consecutive_failures > 3:
        effective_exploration = min(0.7, EXPLORATION_RATE + consecutive_failures * 0.1)
    
    # Decide exploration vs exploitation
    explore = random.random() < effective_exploration
    
    # Generate neighbor
    new_sizing = get_neighbor(current_sizing, exploration=explore)
    
    # Apply to schematic and simulate
    schematic = read_schematic(SCHEMATIC_PATH)
    modified = apply_sizing(schematic, new_sizing)
    write_schematic(SCHEMATIC_PATH, modified)
    
    # Run simulation with retry
    result = run_simulation()
    
    # If simulation failed, try once more with the same sizing
    if not result.success:
        result = run_simulation()
    
    new_score = result.score(TARGETS)
    
    # Record in history
    state.history.append((new_sizing.copy(), result))
    
    # Track failures
    if not result.success:
        return current_sizing, current_score, False, consecutive_failures + 1
    
    # Accept/reject based on simulated annealing criterion
    accepted = False
    if new_score > current_score:
        accepted = True
    else:
        # Accept worse solution with probability based on temperature
        delta = current_score - new_score
        prob = math.exp(-delta / max(temperature, 0.1))
        if random.random() < prob:
            accepted = True
    
    # Update best if this is the best we've seen
    if new_score > state.best_score:
        state.best_score = new_score
        state.best_sizing = new_sizing.copy()
        state.best_result = result
    
    return (new_sizing if accepted else current_sizing, 
            new_score if accepted else current_score, 
            accepted,
            0 if result.success else consecutive_failures + 1)


def gradient_free_optimize(
    state: OptimizationState,
    initial_sizing: TransistorSizing
) -> TransistorSizing:
    """
    Main optimization loop using simulated annealing with adaptive temperature.
    """
    current_sizing = initial_sizing.copy()
    
    # Initial simulation
    schematic = read_schematic(SCHEMATIC_PATH)
    modified = apply_sizing(schematic, current_sizing)
    write_schematic(SCHEMATIC_PATH, modified)
    result = run_simulation()
    current_score = result.score(TARGETS)
    
    state.history.append((current_sizing.copy(), result))
    state.best_sizing = current_sizing.copy()
    state.best_result = result
    state.best_score = current_score
    
    print(f"\n{'='*70}")
    print(f"Initial: Gain={result.gain_db:.1f}dB, UGF={result.ugf/1e3:.1f}kHz, "
          f"PM={result.phase_margin:.1f}°, VB2={result.vb2:.3f}V")
    print(f"Initial Score: {current_score:.2f}")
    print(f"{'='*70}\n")
    
    # Simulated annealing parameters
    initial_temp = 20.0
    final_temp = 0.1
    
    no_improvement_count = 0
    prev_best_score = current_score
    consecutive_failures = 0
    
    for i in range(MAX_ITERATIONS):
        state.iteration = i + 1
        
        # Adaptive temperature cooling
        progress = i / MAX_ITERATIONS
        temperature = initial_temp * (final_temp / initial_temp) ** progress
        
        # Take optimization step
        new_sizing, new_score, accepted, consecutive_failures = simulated_annealing_step(
            state, current_sizing, current_score, temperature, consecutive_failures
        )
        
        if accepted:
            current_sizing = new_sizing
            current_score = new_score
        
        # Get latest result
        latest_result = state.history[-1][1]
        
        # Print progress
        status = "✓" if accepted else "✗"
        best_marker = " ★" if current_score >= state.best_score else ""
        
        if latest_result.success:
            print(f"[{i+1:3d}/{MAX_ITERATIONS}] {status} Gain={latest_result.gain_db:.1f}dB, "
                  f"UGF={latest_result.ugf/1e3:.1f}kHz, VB2={latest_result.vb2:.3f}V, "
                  f"Score={latest_result.score(TARGETS):.1f}{best_marker}")
        else:
            print(f"[{i+1:3d}/{MAX_ITERATIONS}] ✗ Simulation failed: {latest_result.error_msg[:40]}")
        
        # Check for convergence
        if state.best_score > prev_best_score + CONVERGENCE_THRESHOLD:
            no_improvement_count = 0
            prev_best_score = state.best_score
        else:
            no_improvement_count += 1
        
        if no_improvement_count >= ITERATIONS_BEFORE_COOLING:
            print(f"\nConverged after {i+1} iterations (no improvement for {ITERATIONS_BEFORE_COOLING} iterations)")
            break
    
    return state.best_sizing


# ============================================================================
# Reporting Functions  
# ============================================================================

def print_summary(state: OptimizationState):
    """Print optimization summary"""
    print(f"\n{'='*70}")
    print("OPTIMIZATION SUMMARY")
    print(f"{'='*70}")
    
    if state.best_result:
        print(f"\nBest Results:")
        print(f"  Gain:         {state.best_result.gain_db:.2f} dB (target: {TARGETS['gain_db']:.1f} dB)")
        print(f"  UGF:          {state.best_result.ugf/1e3:.2f} kHz (target: {TARGETS['ugf']/1e3:.1f} kHz)")
        print(f"  Phase Margin: {state.best_result.phase_margin:.2f}° (target: ≥{TARGETS['phase_margin']:.1f}°)")
        print(f"  VB1:          {state.best_result.vb1:.3f} V")
        print(f"  VB2:          {state.best_result.vb2:.3f} V (target: {TARGETS['vb2_min']:.2f}-{TARGETS['vb2_max']:.2f} V)")
        print(f"  Score:        {state.best_score:.2f}")
    
    if state.best_sizing:
        print(f"\nBest Transistor Sizing (Active OTA only):")
        print(f"  Stage 1 - Differential Pair:")
        print(f"    x11[{state.best_sizing.diff_pair_1_count-1}:0], x12[{state.best_sizing.diff_pair_2_count-1}:0]")
        print(f"  Stage 1 - Active Loads:")
        print(f"    x15[{state.best_sizing.active_load_1_count-1}:0], x14[{state.best_sizing.active_load_2_count-1}:0]")
        print(f"  Stage 1 - Tail Current:")
        print(f"    x13[{state.best_sizing.current_source_2_count-1}:0]")
        print(f"  Stage 2 - Output Stage:")
        print(f"    x2[{state.best_sizing.stage_2_pmos_count-1}:0], x1[{state.best_sizing.class_a_1_count-1}:0]")
    
    print(f"\nTotal iterations: {len(state.history)}")
    print(f"{'='*70}")


def save_results(state: OptimizationState, filename: str = "optimization_results.json"):
    """Save optimization results to JSON file"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "targets": TARGETS,
        "best_score": state.best_score,
        "best_sizing": state.best_sizing.to_dict() if state.best_sizing else None,
        "best_result": {
            "gain_db": state.best_result.gain_db,
            "ugf": state.best_result.ugf,
            "phase_margin": state.best_result.phase_margin,
            "vb1": state.best_result.vb1,
            "vb2": state.best_result.vb2,
        } if state.best_result else None,
        "history": [
            {
                "sizing": s.to_dict(),
                "result": {
                    "gain_db": r.gain_db,
                    "ugf": r.ugf,
                    "phase_margin": r.phase_margin,
                    "vb2": r.vb2,
                    "score": r.score(TARGETS),
                    "success": r.success,
                }
            }
            for s, r in state.history
        ]
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nResults saved to {filename}")


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    print(f"\n{'='*70}")
    print("OTA OPTIMIZATION SCRIPT (Two-Stage Miller OTA)")
    print(f"{'='*70}")
    print(f"Schematic: {SCHEMATIC_PATH}")
    print(f"Targets: Gain≥{TARGETS['gain_db']}dB, UGF≥{TARGETS['ugf']/1e3:.0f}kHz, PM≥{TARGETS['phase_margin']}°")
    print(f"Max iterations: {MAX_ITERATIONS}")
    print(f"\nNOTE: Only optimizing active OTA components.")
    print(f"      Bias current generator is NOT modified.")
    
    # Initialize state
    state = OptimizationState()
    
    # Starting point - read current values from schematic
    schematic = read_schematic(SCHEMATIC_PATH)
    initial_sizing = parse_sizing_from_schematic(schematic)
    
    print(f"\nParsed initial sizing from schematic:")
    print(f"  Stage 1 - Differential Pair:")
    print(f"    x11={initial_sizing.diff_pair_1_count}, x12={initial_sizing.diff_pair_2_count}")
    print(f"  Stage 1 - Active Loads:")
    print(f"    x15={initial_sizing.active_load_1_count}, x14={initial_sizing.active_load_2_count}")
    print(f"  Stage 1 - Tail Current:")
    print(f"    x13={initial_sizing.current_source_2_count}")
    print(f"  Stage 2 - Output Stage:")
    print(f"    x2={initial_sizing.stage_2_pmos_count}, x1={initial_sizing.class_a_1_count}")
    
    try:
        # Run optimization
        best_sizing = gradient_free_optimize(state, initial_sizing)
        
        # Apply best sizing to schematic
        schematic = read_schematic(SCHEMATIC_PATH)
        modified = apply_sizing(schematic, best_sizing)
        write_schematic(SCHEMATIC_PATH, modified)
        
        # Print summary
        print_summary(state)
        
        # Save results
        save_results(state)
        
    except KeyboardInterrupt:
        print("\n\nOptimization interrupted by user.")
        if state.best_sizing:
            print("Applying best found sizing before exit...")
            schematic = read_schematic(SCHEMATIC_PATH)
            modified = apply_sizing(schematic, state.best_sizing)
            write_schematic(SCHEMATIC_PATH, modified)
            print_summary(state)
            save_results(state)
    
    except Exception as e:
        print(f"\nError during optimization: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
