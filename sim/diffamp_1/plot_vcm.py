#!/usr/bin/env python3
"""Plot DC gain (and optionally UGBW / phase margin) vs VCM.

Reads the CSV produced by ac_vcm.spi and creates a Bode-style
summary that shows which common-mode voltage maximises gain.

Usage:
    python3 plot_vcm.py                         # auto-find CSV
    python3 plot_vcm.py output_ac_vcm/*.csv     # explicit path
"""

import glob
import sys
import os
import numpy as np

# ---------------------------------------------------------------------------
# Locate CSV
# ---------------------------------------------------------------------------
if len(sys.argv) > 1:
    csv_path = sys.argv[1]
else:
    candidates = sorted(glob.glob("output_acvcm/*.csv"))
    if not candidates:
        print("No CSV found in output_ac_vcm/ – run the simulation first.")
        sys.exit(1)
    csv_path = candidates[-1]

print(f"Reading {csv_path}")

# ---------------------------------------------------------------------------
# Parse CSV  (space-separated, first line is header)
# ---------------------------------------------------------------------------
vcm = []
gain = []
ugbw = []
pm = []

with open(csv_path) as f:
    header = f.readline()  # skip header
    for line in f:
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            v = float(parts[0])
            g = float(parts[1])
        except ValueError:
            continue
        vcm.append(v)
        gain.append(g)
        # UGBW and PM may be missing if gain < 0 dB
        try:
            ugbw.append(float(parts[2]) if len(parts) > 2 else float("nan"))
        except ValueError:
            ugbw.append(float("nan"))
        try:
            pm.append(float(parts[3]) if len(parts) > 3 else float("nan"))
        except ValueError:
            pm.append(float("nan"))

vcm = np.array(vcm)
gain = np.array(gain)
ugbw = np.array(ugbw)
pm = np.array(pm)

# ---------------------------------------------------------------------------
# Find optimum
# ---------------------------------------------------------------------------
idx_best = np.argmax(gain)
best_vcm = vcm[idx_best]
best_gain = gain[idx_best]

print(f"\n--- VCM Sweep Results ---")
print(f"{'VCM (V)':>8s}  {'Gain (dB)':>10s}  {'UGBW (MHz)':>10s}  {'PM (deg)':>10s}")
for i in range(len(vcm)):
    flag = " <-- best" if i == idx_best else ""
    u = f"{ugbw[i]*1e-6:.2f}" if not np.isnan(ugbw[i]) else "  n/a"
    p = f"{pm[i]:.1f}" if not np.isnan(pm[i]) else "  n/a"
    print(f"{vcm[i]:8.2f}  {gain[i]:10.1f}  {u:>10s}  {p:>10s}{flag}")

print(f"\nOptimal VCM = {best_vcm:.2f} V  =>  DC gain = {best_gain:.1f} dB")

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots(figsize=(7, 4))

    color_gain = "tab:blue"
    ax1.set_xlabel("VCM  (V)")
    ax1.set_ylabel("DC Gain  (dB)", color=color_gain)
    ax1.plot(vcm, gain, "o-", color=color_gain, label="DC Gain")
    ax1.axvline(best_vcm, color="grey", ls="--", lw=0.8)
    ax1.annotate(
        f"best = {best_vcm:.2f} V\n({best_gain:.1f} dB)",
        xy=(best_vcm, best_gain),
        xytext=(best_vcm + 0.08, best_gain - 3),
        arrowprops=dict(arrowstyle="->", color="grey"),
        fontsize=9,
    )
    ax1.tick_params(axis="y", labelcolor=color_gain)
    ax1.grid(True, alpha=0.3)

    # Secondary axis: UGBW (if available)
    valid_ugbw = ~np.isnan(ugbw)
    if valid_ugbw.any():
        ax2 = ax1.twinx()
        color_ugbw = "tab:red"
        ax2.set_ylabel("UGBW  (MHz)", color=color_ugbw)
        ax2.plot(vcm[valid_ugbw], ugbw[valid_ugbw] * 1e-6, "s--", color=color_ugbw, ms=4, label="UGBW")
        ax2.tick_params(axis="y", labelcolor=color_ugbw)

    fig.tight_layout()
    out_png = os.path.splitext(csv_path)[0] + "_vcm_sweep.png"
    fig.savefig(out_png, dpi=150)
    print(f"Plot saved to {out_png}")

except ImportError:
    print("matplotlib not available – skipping plot.")
