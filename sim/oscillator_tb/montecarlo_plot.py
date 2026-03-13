import csv
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

RESULTS_DIR = "results_12.03.2026"


def read_csv(path):
    """Read a semicolon-delimited CSV and return (temps, freqs_MHz)."""
    temps, freqs = [], []
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
    """Detect outlier runs by checking if any point deviates too far from
    a simple linear fit of that run's own data."""
    if len(temps) < 3:
        return True
    coeffs = np.polyfit(temps, freqs, 1)
    fit = np.polyval(coeffs, temps)
    residuals = np.abs(freqs - fit)
    # Flag as outlier if max residual > 30% of the frequency range
    freq_range = freqs.max() - freqs.min()
    if freq_range < 0.01:
        return True
    return np.max(residuals) > 0.3 * freq_range


# --- Load all MC runs, filter outliers ---
mc_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "mc", "*_oscillator.csv")))
runs = []
outlier_runs = []
for path in mc_files:
    t, f = read_csv(path)
    if len(t) == 0:
        continue
    if is_outlier(t, f):
        outlier_runs.append((t, f, os.path.basename(path)))
    else:
        runs.append((t, f, os.path.basename(path)))

print(f"Loaded {len(runs)} good MC runs, rejected {len(outlier_runs)} outliers")
for _, _, name in outlier_runs:
    print(f"  outlier: {name}")

# --- Print average frequency at min, mid, max temperature ---
all_temps = runs[0][0]
t_min, t_max = all_temps[0], all_temps[-1]
t_mid_idx = np.argmin(np.abs(all_temps - 25))
t_mid = all_temps[t_mid_idx]

for t_target, label in [(t_min, "min"), (t_mid, "mid"), (t_max, "max")]:
    vals = []
    for t, f, _ in runs:
        idx = np.argmin(np.abs(t - t_target))
        vals.append(f[idx])
    avg = np.mean(vals)
    std = np.std(vals)
    print(f"  T={t_target:+.0f}°C ({label}):  avg = {avg:.4f} MHz,  std = {std:.4f} MHz")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Subplot 1: Raw values ---
ax = axes[0]
for t, f, _ in runs:
    ax.plot(t, f, "-", alpha=0.5, linewidth=0.8, color="C0")
ax.set_title(f"Raw Frequency ({len(runs)} runs)")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Frequency [MHz]")
ax.grid(True)

# --- Subplot 2: Offset removed (check linearity) ---
ax = axes[1]
shifted_all = np.array([f - f[0] for t, f, _ in runs])
shifted_mean = np.mean(shifted_all, axis=0)
shifted_min = np.min(shifted_all, axis=0)
shifted_max = np.max(shifted_all, axis=0)
t_common = runs[0][0]
ax.fill_between(t_common, shifted_min, shifted_max, alpha=0.25, color="C2", label="Min–Max range")
ax.plot(t_common, shifted_mean, "-", color="C2", linewidth=1.5, label="Mean")
ax.set_title("Offset Removed (linearity check)")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Δ Frequency [MHz]")
ax.legend(fontsize=7)
ax.grid(True)

# --- Subplot 3: Deviation from linear fit ---
ax = axes[2]
dev_all = []
for t, f, _ in runs:
    coeffs = np.polyfit(t, f, 1)
    fit = np.polyval(coeffs, t)
    dev_all.append((f - fit) * 1e3)  # kHz
dev_all = np.array(dev_all)
dev_mean = np.mean(dev_all, axis=0)
dev_min = np.min(dev_all, axis=0)
dev_max = np.max(dev_all, axis=0)
ax.fill_between(t_common, dev_min, dev_max, alpha=0.25, color="C3", label="Min–Max range")
ax.plot(t_common, dev_mean, "-", color="C3", linewidth=1.5, label="Mean")
ax.set_title("Deviation from Linear Fit")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Deviation [kHz]")
ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
ax.legend(fontsize=7)
ax.grid(True)

fig.suptitle("Oscillator Monte Carlo Analysis", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "montecarlo_freq.png"), dpi=150)
plt.show()
