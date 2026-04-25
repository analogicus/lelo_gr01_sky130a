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
    csv_path = "final_results/lay/csv/tran_LayGtKttmmTtVt_oscillator.csv"

temps, freqs = read_csv(csv_path)
freqs_mhz = freqs / 1e6

# Polynomial Regressions
print("Polynomial Regressions (freq_MHz as function of temperature):")
print("=" * 70)
for order in range(1, 7):
    coeffs_n = np.polyfit(temps, freqs_mhz, order)
    fit_n = np.polyval(coeffs_n, temps)
    residual = freqs_mhz - fit_n
    max_err = np.max(np.abs(residual))
    rms_err = np.sqrt(np.mean(residual**2))
    terms = [f"{c:+.6e}*T^{order-i}" if order-i > 1 else (f"{c:+.6e}*T" if order-i == 1 else f"{c:+.6e}") for i, c in enumerate(coeffs_n)]
    print(f"\nOrder {order}:\n  f(T) = {' '.join(terms)}\n  Max error: {max_err:.6f} MHz, RMS error: {rms_err:.6f} MHz")
print("=" * 70)

# Linear fit calculations
temp_per_mhz = np.polyfit(temps, freqs_mhz, 1)
linear_fit = np.polyval(temp_per_mhz, temps)
error = freqs_mhz - linear_fit
error_temp = error / temp_per_mhz[0]  

# --- PLOTTING START ---
# We must define 'fig' and 'axes' here so they are available below
fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# Top Plot
ax0 = axes[0]
ax0.plot(temps, freqs_mhz, "o-", color="C0", markersize=4, label="Measured")
ax0.plot(temps, linear_fit, "--", color="C3", label=f"Linear fit ({temp_per_mhz[0]:.4f} MHz/°C)")
ax0.set_ylabel("Frequency [MHz]")
ax0.set_title("Oscillator Frequency vs Temperature")
ax0.legend()
ax0.grid(True)

# Bottom Plot
ax1 = axes[1]
ax1.bar(temps, error_temp, width=8, color="C1", edgecolor="black", linewidth=0.5)
ax1.axhline(0, color="black", linewidth=0.5)

# Tangent line logic for 0-70C
mask = (temps >= 0) & (temps <= 70)
if np.any(mask):
    sub_errors = error_temp[mask]
    idx_max = np.argmax(np.abs(sub_errors))
    max_val = sub_errors[idx_max]

    # Draw the tangent line
    ax1.axhline(max_val, color="red", linestyle="--", linewidth=1.5, alpha=0.8)
    
    # Label the tangent line
    offset = 0.2 if max_val >= 0 else -0.4
    ax1.text(np.mean(temps), max_val + offset, 
             f"Max Error (0-70°C): {max_val:.2f}°C", 
             color="red", fontweight="bold", ha="center",
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1))

ax1.set_xlabel("Temperature [°C]")
ax1.set_ylabel("Linearity Error [°C]")
ax1.set_title(f"Linearity Error (Full Range Max: {np.max(np.abs(error_temp)):.2f}°C)")
ax1.grid(True, axis="y")

plt.tight_layout()
out_dir = os.path.dirname(csv_path) or "."
plt.savefig(os.path.join(out_dir, "linearity_error.png"), dpi=150)
plt.show()
