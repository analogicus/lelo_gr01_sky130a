import csv
import glob
import os
import matplotlib.pyplot as plt

RESULTS_DIR = "results_mc_pwrup_27.03.26"


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
    return temps, freqs


fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)

# --- Typical ---
ax = axes[0]
typ_path = os.path.join(RESULTS_DIR, "oscillator_typical.csv")
t, f = read_csv(typ_path)
ax.plot(t, f, "o-", color="C0", markersize=3)
ax.set_title("Typical")
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Frequency [MHz]")
ax.grid(True)

# --- ETC (Extreme Test Conditions) ---
ax = axes[1]
etc_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "etc", "*_oscillator.csv")))
for path in etc_files:
    label = os.path.basename(path).replace("_oscillator.csv", "").replace("tran_SchGt", "")
    t, f = read_csv(path)
    ax.plot(t, f, "o-", markersize=2, label=label)
ax.set_title(f"Extreme Test Conditions ({len(etc_files)} corners)")
ax.set_xlabel("Temperature [°C]")
ax.grid(True)
ax.legend(fontsize=6, ncol=2)

# --- Monte Carlo ---
ax = axes[2]
mc_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "mc", "*_oscillator.csv")))
for path in mc_files:
    t, f = read_csv(path)
    ax.plot(t, f, "-", alpha=0.4, linewidth=0.8, color="C1")
ax.set_title(f"Monte Carlo ({len(mc_files)} runs)")
ax.set_xlabel("Temperature [°C]")
ax.grid(True)

fig.suptitle("Oscillator Frequency vs Temperature", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, "oscillator_freq.png"), dpi=150)
plt.show()
