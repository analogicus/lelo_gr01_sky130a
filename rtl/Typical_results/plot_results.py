import csv
import numpy as np
import matplotlib.pyplot as plt
import os

temps = []
counts = []
freqs = []

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "results.csv")

with open(csv_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row["temperature_C"]))
        counts.append(int(row["count"]))
        freqs.append(float(row["freq_MHz"]))

temps = np.array(temps)
counts = np.array(counts)
freqs = np.array(freqs)

# Theoretical: count = CLK_FREQ / freq_osc
# freq_osc_theory is based off a linear approximation from the same one as the oscillator sim
freq_osc_theory = +8.602795e-03*temps +1.850301e+00
counts_theory = freq_osc_theory / 0.032768
pct_error_vs_perfect_linear = (counts - counts_theory) / counts_theory * 100


counts_float = freqs / 0.032768
pct_error_vs_float = (counts - counts_float) / counts_float * 100

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle(f"LELO_TEMP Typical Run Analysis", fontsize=14, fontweight='bold')

# Top left: Frequency vs Temperature
ax = axes[0, 0]
ax.plot(temps, freqs, "o-", markersize=2, label="Measured")
ax.plot(temps, freq_osc_theory, "--", color="C3", label="Theoretical")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Frequency (MHz)")
ax.set_title("Oscillator Frequency vs Temperature")
ax.legend()
ax.grid(True)

# Top right: Count vs Temperature
ax = axes[0, 1]
ax.plot(temps, counts, "o-", markersize=2, label="Measured")
ax.plot(temps, counts_float, "--", color="C3", label="Theoretical, based on measured frequency")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Count")
ax.set_title("Clock Count vs Temperature")
ax.legend()
ax.grid(True)

# Bottom left: Absolute error
ax = axes[1, 0]
ax.bar(temps, pct_error_vs_perfect_linear, width=0.8, color="C1", edgecolor="black", linewidth=0.3)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Error (%)")
ax.set_title(f"Error compared to perfectly linear system, full system (max {np.max(np.abs(pct_error_vs_perfect_linear)):.1f}%)")
ax.grid(True, axis="y")

# Bottom right: Relative error
ax = axes[1, 1]
ax.bar(temps, pct_error_vs_float, width=0.8, color="C2", edgecolor="black", linewidth=0.3)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Error (%)")
ax.set_title(f"Relative Error, analog error removed (max {np.max(np.abs(pct_error_vs_float)):.2f}%)")
ax.grid(True, axis="y")

plt.tight_layout()
plt.savefig(os.path.join(current_dir, "results.png"), dpi=150)
plt.show()
