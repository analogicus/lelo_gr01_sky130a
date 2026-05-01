import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import re
from pathlib import Path

def plot_vref_combined(data_dir="final_results/sch/csv", file_pattern="tran_*_oscillator.csv"):
    # 1. Setup search path
    search_path = os.path.join(data_dir, file_pattern)
    files = glob.glob(search_path)
    
    if not files:
        print(f"No CSV files found in {search_path}")
        return

    files.sort()

    # 2. Setup Single Plot
    plt.figure(figsize=(12, 8))
    colors = plt.cm.tab10.colors 
    sim_type = "Unknown"

    for i, file_path in enumerate(files):
        filename = Path(file_path).name
        
        # Determine Sim Type for Title (Check for Sch or Lay)
        if "Sch" in filename:
            sim_type = "Schematic-Based (Pre-LPE)"
        elif "Lay" in filename:
            sim_type = "Layout-Based (Post-LPE)"

        # Regex to extract specific parts: 
        # (Kss|Kfs|Ksf|Kff) -> Group 1
        # (Vh|Vl) -> Group 2
        match = re.search(r'K(ss|fs|sf|ff)Th(Vh|Vl)', filename, re.IGNORECASE)
        
        if match:
            corner = match.group(1).upper()
            voltage = match.group(2).upper()
            legend_label = f"{corner} {voltage}"
        else:
            # Fallback if regex fails
            legend_label = filename

        try:
            # Read data
            df = pd.read_csv(file_path, sep=';', skipinitialspace=True)
            df.columns = df.columns.str.strip()

            # Plotting
            plt.plot(df['Temp'], df['Vref'], label=legend_label, linewidth=2, color=colors[i % 10])
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # 3. Aesthetics
    plt.title(f"VREF Overlay: All Process Corners\n{sim_type}", fontsize=16, fontweight='bold')
    plt.xlabel("Temperature (°C)", fontsize=12)
    plt.ylabel("VREF (V)", fontsize=12)
    
    # Highlight Target Window
    plt.axvspan(0, 70, color='gray', alpha=0.1, label='Target Range (0-70C)')
    
    # Calibration Lines
    plt.axvline(x=25, color='red', linestyle='--', alpha=0.5, label='Cal Point (25C)')
    plt.axvline(x=85, color='red', linestyle='--', alpha=0.5, label='Cal Point (85C)')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    plot_vref_combined()
