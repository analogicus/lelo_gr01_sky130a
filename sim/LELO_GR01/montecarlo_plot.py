import csv
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration ---
RESULTS_DIR = "output_tran"
# Specify the filename (including extension) you want to ignore
file_to_omit = "None" 

def read_csv(path):
    """Read a semicolon-delimited CSV and return (temps, freqs_MHz)."""
    temps, freqs = [], []
    if not os.path.exists(path): return np.array([]), np.array([])
    with open(path) as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            if len(row) < 2 or row[1].strip() == "":
                continue
            temps.append(float(row[0].strip()))
            freqs.append(float(row[1].strip()) / 1e6)
    return np.array(temps), np.array(freqs)

def is_outlier(temps, freqs):
    if len(temps) < 3: return True
    coeffs = np.polyfit(temps, freqs, 1)
    fit = np.polyval(coeffs, temps)
    residuals = np.abs(freqs - fit)
    freq_range = freqs.max() - freqs.min()
    if freq_range < 0.01: return True
    return np.max(residuals) > 0.3 * freq_range

# ---- 1. Gather ALL files (MC and Corners) ----
all_csv_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "**", "tran_Lay*_oscillator.csv"), recursive=True))

# --- NEW: Filter out the specific file ---
if file_to_omit:
    original_count = len(all_csv_files)
    all_csv_files = [f for f in all_csv_files if os.path.basename(f) != file_to_omit]
    if len(all_csv_files) < original_count:
        print(f"Successfully omitted: {file_to_omit}")

runs = []
outlier_runs = []
for path in all_csv_files:
    t, f = read_csv(path)
    if len(t) == 0: continue
    name = os.path.basename(path).replace("_oscillator.csv", "")
    if is_outlier(t, f):
        outlier_runs.append((t, f, name))
    else:
        runs.append((t, f, name))

print(f"Loaded {len(runs)} good runs, rejected {len(outlier_runs)} outliers")

if not runs:
    print("No valid data runs to plot. Check your data directory or skip settings.")
    exit()

# Setup Figure
fig, axes = plt.subplots(1, 3, figsize=(18, 8)) 

t_common = runs[0][0]

# --- Subplot 1: Raw values ---
ax = axes[0]
colors = plt.cm.tab20(np.linspace(0, 1, len(runs)))
for i, (t, f, name) in enumerate(runs):
    lw = 2.0 if "Ktt" in name else 0.7
    alpha = 1.0 if "Ktt" in name else 0.6
    ax.plot(t, f, "-", alpha=alpha, linewidth=lw, color=colors[i], label=name)

ax.set_title(f"Raw Frequency ({len(runs)} runs)")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Frequency [MHz]")
ax.grid(True, linestyle=':', alpha=0.6)

# --- Subplot 2: Offset removed ---
ax = axes[1]
shifted_all = np.array([f - f[0] for t, f, _ in runs])
shifted_mean = np.mean(shifted_all, axis=0)
ax.fill_between(t_common, np.min(shifted_all, axis=0), np.max(shifted_all, axis=0), alpha=0.2, color="C2")
ax.plot(t_common, shifted_mean, "-", color="C2", linewidth=1.5)
ax.set_title("Offset Removed")
ax.set_xlabel("Temperature [°C]")
ax.grid(True, linestyle=':', alpha=0.6)

# --- Subplot 3: Deviation from linear fit ---
ax = axes[2]
dev_all = []
for t, f, _ in runs:
    coeffs = np.polyfit(t, f, 1)
    fit = np.polyval(coeffs, t)
    dev_all.append((f - fit) * 1e3) 
dev_all = np.array(dev_all)
ax.fill_between(t_common, np.min(dev_all, axis=0), np.max(dev_all, axis=0), alpha=0.2, color="C3")
ax.plot(t_common, np.mean(dev_all, axis=0), "-", color="C3", linewidth=1.5)
ax.set_title("Deviation from Linear Fit")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Error [kHz]")
ax.grid(True, linestyle=':', alpha=0.6)

# ---- THE GLOBAL HORIZONTAL LEGEND ----
handles, labels = axes[0].get_legend_handles_labels()

fig.legend(
    handles, 
    labels, 
    loc='lower center', 
    ncol=12, 
    mode="expand", 
    fontsize='xx-small', 
    frameon=True,
    borderaxespad=0.5,
    bbox_to_anchor=(0.05, 0.02, 0.9, 0.1)
)

fig.suptitle("Oscillator Analysis: All Corners & Monte Carlo", fontsize=14, fontweight='bold')
plt.subplots_adjust(bottom=0.25, top=0.90, wspace=0.3, left=0.06, right=0.96)

plt.savefig(os.path.join(RESULTS_DIR, "full_analysis_plot.png"), dpi=200)
plt.show()
