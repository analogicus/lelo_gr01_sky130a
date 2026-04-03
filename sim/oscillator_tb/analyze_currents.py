#!/usr/bin/env python3
"""Analyze transistor drain currents in the first 0.5us from ngspice raw file."""

import struct
import numpy as np
import sys

def parse_raw(filename):
    """Parse ngspice binary raw file."""
    with open(filename, 'rb') as f:
        raw = f.read()

    # Find the header (ASCII until "Binary:\n")
    header_end = raw.find(b'Binary:\n')
    if header_end < 0:
        print("ERROR: Could not find 'Binary:' marker in raw file")
        sys.exit(1)

    header = raw[:header_end].decode('ascii')
    binary_data = raw[header_end + len(b'Binary:\n'):]

    # Parse header
    variables = []
    num_points = 0
    num_vars = 0
    in_variables = False

    for line in header.split('\n'):
        line = line.strip()
        if line.startswith('No. Points:'):
            num_points = int(line.split(':')[1].strip())
        elif line.startswith('No. Variables:'):
            num_vars = int(line.split(':')[1].strip())
        elif line.startswith('Variables:'):
            in_variables = True
            continue
        elif line.startswith('Values:') or line.startswith('Binary:'):
            in_variables = False
        elif in_variables and line:
            parts = line.split()
            if len(parts) >= 3:
                idx = int(parts[0])
                name = parts[1]
                vtype = parts[2]
                variables.append((idx, name, vtype))

    print(f"Number of variables: {num_vars}")
    print(f"Number of points: {num_points}")

    # Parse binary data - ngspice uses double precision (8 bytes per value)
    # Total data = num_points * num_vars * 8 bytes
    expected_bytes = num_points * num_vars * 8
    print(f"Binary data size: {len(binary_data)} bytes, expected: {expected_bytes}")

    # The raw file may have multiple plots (the initial tran + the temp sweeps)
    # We want the first plot (tran 0.5n 4u)
    data = np.frombuffer(binary_data[:expected_bytes], dtype=np.float64)
    data = data.reshape(num_points, num_vars)

    return variables, data, num_points

def main():
    raw_file = "output_tran/tran_SchGtKttTtVt.raw"
    variables, data, num_points = parse_raw(raw_file)

    # Find time variable
    time_idx = None
    for idx, name, vtype in variables:
        if name == 'time':
            time_idx = idx
            break

    if time_idx is None:
        print("ERROR: Could not find 'time' variable")
        sys.exit(1)

    time = data[:, time_idx]
    print(f"\nTime range: {time[0]*1e6:.4f} us to {time[-1]*1e6:.4f} us")

    # Trim first 10ns (simulator startup instabilities) and last 10ns before PWRUP at 0.5us
    t_start = 10e-9
    t_stop = 0.49e-6
    mask = (time >= t_start) & (time <= t_stop)
    if not np.any(mask):
        print(f"No data points in {t_start*1e9:.0f}ns - {t_stop*1e6:.2f}us window!")
        sys.exit(1)

    print(f"Data points in {t_start*1e9:.0f}ns - {t_stop*1e6:.2f}us window: {np.sum(mask)}")

    # Find all current variables (transistor drain currents)
    # ngspice saves currents as @device[id] for MOSFETs
    current_vars = []
    for idx, name, vtype in variables:
        if 'current' in vtype.lower() or name.startswith('@') or name.startswith('i('):
            current_vars.append((idx, name, vtype))

    # Also look for any variable with 'i(' prefix which are branch currents
    if not current_vars:
        # Try broader search
        for idx, name, vtype in variables:
            if '[i' in name.lower() or 'i(' in name.lower():
                current_vars.append((idx, name, vtype))

    print(f"\nFound {len(current_vars)} current variables")

    if not current_vars:
        print("\nAll variable names:")
        for idx, name, vtype in variables[:50]:
            print(f"  {idx}: {name} ({vtype})")
        if len(variables) > 50:
            print(f"  ... and {len(variables)-50} more")
        sys.exit(0)

    # Compute signed and absolute current stats in the analysis window
    results = []
    for idx, name, vtype in current_vars:
        curr = data[mask, idx]
        avg_signed = np.mean(curr)
        avg_abs = np.mean(np.abs(curr))
        peak_abs = np.max(np.abs(curr))
        results.append((name, avg_signed, avg_abs, peak_abs))

    # Sort by absolute signed mean (true DC component, descending)
    results.sort(key=lambda x: abs(x[1]), reverse=True)

    def fmt(v):
        """Format absolute value with units."""
        if v >= 1e-3:
            return f"{v*1e3:.3f} mA"
        elif v >= 1e-6:
            return f"{v*1e6:.3f} uA"
        elif v >= 1e-9:
            return f"{v*1e9:.3f} nA"
        else:
            return f"{v*1e12:.3f} pA"

    def fmts(v):
        """Format signed value with units."""
        sign = '+' if v >= 0 else '-'
        av = abs(v)
        if av >= 1e-3:
            return f"{sign}{av*1e3:.3f} mA"
        elif av >= 1e-6:
            return f"{sign}{av*1e6:.3f} uA"
        elif av >= 1e-9:
            return f"{sign}{av*1e9:.3f} nA"
        else:
            return f"{sign}{av*1e12:.3f} pA"

    print(f"\n{'='*110}")
    print(f"Transistor/Device currents during {t_start*1e9:.0f}ns-{t_stop*1e6:.2f}us (sorted by |DC| component)")
    print(f"{'='*110}")
    print(f"{'Signal Name':<55} {'DC (signed)':>14} {'Avg |I|':>14} {'Peak |I|':>14} {'AC?':>6}")
    print(f"{'-'*110}")

    for name, avg_s, avg_a, peak in results:
        if avg_a > 1e-12:  # Only show currents > 1pA
            ac_ratio = avg_a / abs(avg_s) if abs(avg_s) > 1e-18 else float('inf')
            ac_flag = ' *AC*' if ac_ratio > 2.0 else ''
            print(f"{name:<55} {fmts(avg_s):>14} {fmt(avg_a):>14} {fmt(peak):>14} {ac_flag:>6}")

    # Separate into categories
    supply_currents = []
    mosfet_currents = []
    bjt_currents = []
    cap_currents = []
    res_currents = []
    other_currents = []

    for name, avg_s, avg_a, peak in results:
        if avg_a < 1e-12:
            continue
        if name.startswith('i(v'):
            supply_currents.append((name, avg_s, avg_a, peak))
        elif '@m.' in name and '[id]' in name:
            mosfet_currents.append((name, avg_s, avg_a, peak))
        elif '@q.' in name:
            bjt_currents.append((name, avg_s, avg_a, peak))
        elif '@c.' in name:
            cap_currents.append((name, avg_s, avg_a, peak))
        elif '@r.' in name:
            res_currents.append((name, avg_s, avg_a, peak))
        else:
            other_currents.append((name, avg_s, avg_a, peak))

    def decode_hier(name):
        """Map hierarchical instance path to readable block names."""
        # xdut.x7 = bandgap, xdut.x8 = oscillator
        desc = name
        if 'xdut.x7' in name:
            desc = "[BANDGAP] " + name
            if 'xdut.x7.x1' in name:
                desc = "[BANDGAP/diffamp_2] " + name
            elif 'xdut.x7.x5' in name and '.xm1' in name:
                desc = "[BANDGAP/pch_mirror_VIN] " + name
            elif 'xdut.x7.x3<' in name and '.xm1' in name:
                desc = "[BANDGAP/pch_mirror_VIP] " + name
            elif 'xdut.x7.xq2' in name:
                desc = "[BANDGAP/Q2_pnp] " + name
            elif 'xdut.x7.xq1<' in name:
                desc = "[BANDGAP/Q1_pnp_array] " + name
            elif 'xdut.x7.x4<' in name:
                desc = "[BANDGAP/nch_cascode] " + name
            elif 'xdut.x7.x6<' in name:
                desc = "[BANDGAP/nch_mirror] " + name
            elif 'xdut.x7.x16' in name:
                desc = "[BANDGAP/pch_startup_pullup] " + name
            elif 'xdut.x7.x17' in name or 'xdut.x7.x19' in name or 'xdut.x7.x20' in name or 'xdut.x7.x21' in name or 'xdut.x7.x22' in name or 'xdut.x7.x23' in name or 'xdut.x7.x24' in name or 'xdut.x7.x25' in name:
                desc = "[BANDGAP/pch_startup_chain] " + name
            elif 'xdut.x7.x18' in name:
                desc = "[BANDGAP/nch_startup] " + name
        elif 'xdut.x8' in name:
            desc = "[OSCILLATOR] " + name
            if 'xdut.x8.x1' in name:
                desc = "[OSC/diffamp_2] " + name
            elif 'xdut.x8.x3' in name:
                desc = "[OSC/not_gate] " + name
            elif 'xdut.x8.x4' in name:
                desc = "[OSC/nch_IBP_gate] " + name
            elif 'xdut.x8.x5' in name:
                desc = "[OSC/DFF] " + name
            elif 'xdut.x8.x6' in name:
                desc = "[OSC/nch_IBP_pwrdn] " + name
            elif 'xdut.x8.x2' in name:
                desc = "[OSC/NOR_gate] " + name
        return desc

    def print_section(title, items, show_hier=False):
        print(f"\n{'='*110}")
        print(f"{title} ({t_start*1e9:.0f}ns - {t_stop*1e6:.2f}us)")
        print(f"  DC = signed mean (true net current flow), |Avg| = mean of absolute, *AC* = mostly oscillation")
        print(f"{'='*110}")
        for name, avg_s, avg_a, peak in items:
            ac_ratio = avg_a / abs(avg_s) if abs(avg_s) > 1e-18 else float('inf')
            ac_flag = ' *AC*' if ac_ratio > 2.0 else ''
            if show_hier:
                desc = decode_hier(name)
                print(f"  {desc}")
                print(f"    DC={fmts(avg_s):>14}  |Avg|={fmt(avg_a):>12}  Peak={fmt(peak):>12}{ac_flag}")
            else:
                print(f"  {name:<55} DC={fmts(avg_s):>14}  |Avg|={fmt(avg_a):>12}  Peak={fmt(peak):>12}{ac_flag}")

    print_section("SUPPLY CURRENTS", supply_currents)
    print_section("MOSFET DRAIN CURRENTS (Id)", mosfet_currents, show_hier=True)
    print_section("BJT CURRENTS", bjt_currents, show_hier=True)

if __name__ == '__main__':
    main()
