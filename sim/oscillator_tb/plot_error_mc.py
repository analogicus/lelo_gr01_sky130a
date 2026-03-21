import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# --- Configuration ---
# This looks in your current directory and subdirectories for the oscillator csvs
data_dir = "output_tran/" 
file_pattern = "*_oscillator.csv"

def parse_data(filename):
    measurements = []
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line_split = line.split(";")
        if len(line_split) == 2:
            try:
                measurements.append([float(line_split[0]), float(line_split[1])])
            except ValueError:
                continue
    return np.array(measurements)

# ---- 1. Gather All Files ----
# This grabs every oscillator CSV in the folder
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))

if not all_files:
    print(f"No files found in {data_dir} matching {file_pattern}")
    exit()

# ---- 2. Processing and Plotting ----
plt.figure(figsize=(14, 8))

# Define a colormap to give every corner a unique color
colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(all_files)))

error_data_for_spread = []
temp_axis = None

for i, file_path in enumerate(all_files):
    data = parse_data(file_path)
    if data is None or len(data) == 0:
        continue
    
    x, y = data[:, 0], data[:, 1]
    if temp_axis is None:
        temp_axis = x
    
    # Linear Regression
    a, b = np.polyfit(x, y, 1)
    measured_temp = (y - b) / a
    error = measured_temp - x
    error_data_for_spread.append(error)
    
    # Determine if this is the "Typical" run to make it stand out
    # Typical usually has 'KttTtVt' in the name
    corner_name = os.path.basename(file_path).replace("_oscillator.csv", "")
    
    if "KttTtVt" in corner_name and "mm" not in corner_name:
        # Plot Typical: Thick, Solid Red
        plt.plot(x, error, color='red', linewidth=3, label=f"TYPICAL ({corner_name})", zorder=100)
    else:
        # Plot Corners/MC: Thin, Dotted, Unique Color
        plt.plot(x, error, color=colors[i], linestyle=':', linewidth=1.2, label=corner_name, alpha=0.8)

# ---- 3. Compute and Plot the Min/Max Spread Area ----
if error_data_for_spread:
    all_errs = np.array(error_data_for_spread)
    y_max = np.max(all_errs, axis=0)
    y_min = np.min(all_errs, axis=0)
    plt.fill_between(temp_axis, y_max, y_min, color='gray', alpha=0.1, label="Corner Spread Range")

# ---- 4. Final Formatting ----
plt.xlabel("Actual Temperature (°C)", fontsize=12)
plt.ylabel("Temperature Measurement Error (°C)", fontsize=12)
plt.title("Temperature Sensor Error: All Corners & Monte Carlo", fontsize=14, fontweight='bold')
plt.grid(True, which='both', linestyle='--', alpha=0.4)

# Place legend below the plot in 3 columns to fit all corner names
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=8, fontsize='x-small', frameon=True)

plt.tight_layout()
plt.show()
