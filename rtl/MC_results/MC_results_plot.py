import csv
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.dirname(os.path.abspath(__file__))

def read_csv(path):
    """Read a comma-delimited results CSV and return (temps, counts, freqs_MHz)."""
    temps, counts, freqs = [], [], []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            temps.append(float(row["temperature_C"]))
            counts.append(int(row["count"]))
            freqs.append(float(row["freq_MHz"]))
    return np.array(temps), np.array(counts), np.array(freqs)

# Load all MC result CSVs
csv_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "results_mc_*.csv")))
runs = []
for path in csv_files:
    t, c, f = read_csv(path)
    name = os.path.basename(path).replace(".csv", "")
    runs.append((t, c, f, name))

print(f"Loaded {len(runs)} MC runs")

t_common = runs[0][0]
all_counts = np.array([c for _, c, _, _ in runs])
all_freqs = np.array([f for _, _, f, _ in runs])

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle(f"LELO_TEMP Monte Carlo Analysis ({len(runs)} runs)", fontsize=14, fontweight='bold')

# --- Subplot 1: Raw count values ---
ax = axes[0]
for t, c, f, name in runs:
    ax.plot(t, c, "-", alpha=0.5, linewidth=0.8)
ax.fill_between(t_common, np.min(all_counts, axis=0), np.max(all_counts, axis=0),
                alpha=0.15, color="C0", label="Min-Max range")
ax.plot(t_common, np.mean(all_counts, axis=0), "-", color="C0", linewidth=2, label="Mean")
ax.set_title(f"Raw Count ({len(runs)} runs)")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Count")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

# --- Subplot 2: Offset removed (linearity check) ---
ax = axes[1]
shifted_all = np.array([c - c[0] for _, c, _, _ in runs])
shifted_mean = np.mean(shifted_all, axis=0)
ax.fill_between(t_common, np.min(shifted_all, axis=0), np.max(shifted_all, axis=0),
                alpha=0.2, color="C2", label="Min-Max range")
ax.plot(t_common, shifted_mean, "-", color="C2", linewidth=1.5, label="Mean")
ax.set_title("Offset Removed (linearity check)")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("\u0394 Count")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

# --- Subplot 3: Deviation from linear fit ---
ax = axes[2]
dev_all = []
for t, c, f, _ in runs:
    coeffs = np.polyfit(t, c.astype(float), 1)
    fit = np.polyval(coeffs, t)
    dev_all.append(c - fit)
dev_all = np.array(dev_all)
ax.fill_between(t_common, np.min(dev_all, axis=0), np.max(dev_all, axis=0),
                alpha=0.2, color="C3", label="Min-Max range")
ax.plot(t_common, np.mean(dev_all, axis=0), "-", color="C3", linewidth=1.5, label="Mean")
ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
ax.set_title("Deviation from Linear Fit")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Error [counts]")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "MC_results_plot.png"), dpi=200)
plt.show()
