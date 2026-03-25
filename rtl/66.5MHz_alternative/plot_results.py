import csv
import numpy as np
import matplotlib.pyplot as plt

temps = []
counts = []
freqs = []

with open("results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row["temperature_C"]))
        counts.append(int(row["count"]))
        freqs.append(float(row["freq_MHz"]))

temps = np.array(temps)
counts = np.array(counts)
freqs = np.array(freqs)

# Theoretical: count = MAX_PULSES * CLK_FREQ / freq_osc
# freq_osc = 1.5 + 0.0093 * (T + 40) MHz,  CLK = 66.5MHz, MAX_PULSES = 16
freq_osc_theory = 1.5 + 0.0093 * (temps + 40.0)
counts_theory = 16 * 66.5 / freqs

abs_error = counts - counts_theory
rel_error = abs_error / counts_theory * 100

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Top left: Frequency vs Temperature
ax = axes[0, 0]
ax.plot(temps, freqs, markersize=2, label="Measured")
ax.plot(temps, freq_osc_theory, "--", color="C3", label="Theoretical")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Frequency (MHz)")
ax.set_title("Oscillator Frequency vs Temperature")
ax.legend()
ax.grid(True)

# Top right: Count vs Temperature
ax = axes[0, 1]
ax.plot(temps, counts, markersize=2, label="Measured")
ax.plot(temps, counts_theory, "--", color="C3", label="Theoretical")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Count")
ax.set_title("Clock Count vs Temperature")
ax.legend()
ax.grid(True)

# Bottom left: Absolute error
ax = axes[1, 0]
ax.bar(temps, abs_error, width=0.8, color="C1", edgecolor="black", linewidth=0.3)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Absolute Error (counts)")
ax.set_title(f"Absolute Error (max {np.max(np.abs(abs_error)):.1f})")
ax.grid(True, axis="y")

# Bottom right: Relative error
ax = axes[1, 1]
ax.bar(temps, rel_error, width=0.8, color="C2", edgecolor="black", linewidth=0.3)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Relative Error (%)")
ax.set_title(f"Relative Error (max {np.max(np.abs(rel_error)):.2f}%)")
ax.grid(True, axis="y")

plt.tight_layout()
plt.savefig("results.png", dpi=150)
plt.show()
