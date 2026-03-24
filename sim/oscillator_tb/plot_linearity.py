import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def read_csv(path):
    """Read a semicolon-delimited CSV and return (temps, freqs)."""
    temps, freqs = [], []
    with open(path) as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            if len(row) < 2 or row[1].strip() == "":
                continue
            temps.append(float(row[0].strip()))
            freqs.append(float(row[1].strip()))
    return np.array(temps), np.array(freqs)


if len(sys.argv) > 1:
    csv_path = sys.argv[1]
else:
    csv_path = "output_tran/tran_SchGtKttTtVt_oscillator.csv"

temps, freqs = read_csv(csv_path)
freqs_mhz = freqs / 1e6

# Linear fit
coeffs = np.polyfit(temps, freqs_mhz, 1)
linear_fit = np.polyval(coeffs, temps)

# Linearity error
error = freqs_mhz - linear_fit
error_pct = error / (linear_fit.max() - linear_fit.min()) * 100

temp_span = temps.max() - temps.min()
error_temp = error_pct / temp_span * 100  # Error as % of temperature span

fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- Frequency vs Temperature with linear fit ---
ax = axes[0]
ax.plot(temps, freqs_mhz, "o-", color="C0", markersize=4, label="Measured")
ax.plot(temps, linear_fit, "--", color="C3", label=f"Linear fit ({coeffs[0]:.4f} MHz/°C)")
ax.set_ylabel("Frequency [MHz]")
ax.set_title("Oscillator Frequency vs Temperature")
ax.legend()
ax.grid(True)

# --- Linearity error ---
ax = axes[1]
ax.bar(temps, error_temp, width=8, color="C1", edgecolor="black", linewidth=0.5)
ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("Temperature [°C]")
ax.set_ylabel("Linearity Error [°C]")
ax.set_title(f"Linearity Error (max {np.max(np.abs(error_temp)):.2f}°C)")
ax.grid(True, axis="y")

plt.tight_layout()

out_dir = os.path.dirname(csv_path) or "."
plt.savefig(os.path.join(out_dir, "linearity_error.png"), dpi=150)
plt.show()
