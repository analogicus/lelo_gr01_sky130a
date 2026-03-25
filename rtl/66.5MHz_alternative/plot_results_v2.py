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

# Theoretical: count = CLK_FREQ / freq_osc
# freq_osc = 1.5 + 0.0093 * (T + 40) MHz,  CLK = 32.768 kHz = 0.032768 MHz
freq_osc_theory = +8.602795e-03*temps +1.850301e+00
counts_theory = 16 * 66.5 / freq_osc_theory
pct_error_vs_perfect_linear = (counts - counts_theory) / counts_theory * 100


counts_float = 16 * 66.5 / freqs
pct_error_vs_float = (counts - counts_float) / counts_float * 100

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

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
ax.set_title(f"Error compared to perfectly linear system (max {np.max(np.abs(pct_error_vs_perfect_linear)):.1f}%)")
ax.grid(True, axis="y")

# Bottom right: Relative error
ax = axes[1, 1]
ax.bar(temps, pct_error_vs_float, width=0.8, color="C2", edgecolor="black", linewidth=0.3)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Error (%)")
ax.set_title(f"Relative Error compared to measured frequency (max {np.max(np.abs(pct_error_vs_float)):.2f}%)")
ax.grid(True, axis="y")

plt.tight_layout()
plt.savefig("results.png", dpi=150)
plt.show()
