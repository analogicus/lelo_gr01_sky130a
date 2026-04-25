import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# --- Configuration ---
data_dir = "output_tran/" 
file_pattern = "tran_Lay*_oscillator.csv"
file_to_skip = "None" 

# --- THREE TOGGLES ---
# 1. Plot Range: "full" (-40 to 125°C) or "0-70" (0 to 70°C)
plot_mode = "0-70" 

# 2. Calibration Type: "1-point" (shared slope) or "2-point" (individual slopes)
cal_mode = "1-point" 

# 3. Fit Method: "best-fit" (minimized error) or "fixed" (force zero error at 0 and 70°C)
fit_method = "fixed"

def parse_data(filename):
    measurements = []
    if not os.path.exists(filename): return None
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line_split = line.split(";")
        if len(line_split) >= 2: 
            try:
                measurements.append([float(line_split[0]), float(line_split[1])])
            except ValueError: continue
    return np.array(measurements)

# ---- 1. Gather Files & Golden Slope for 1-Point ----
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))
if file_to_skip and file_to_skip != "None":
    all_files = [f for f in all_files if os.path.basename(f) != file_to_skip]

golden_slope = None
if cal_mode == "1-point":
    ref_file = next((f for f in all_files if "KttTtVt" in f and "mm" not in f), all_files[0])
    ref_data = parse_data(ref_file)
    if ref_data is not None:
        if fit_method == "best-fit":
            golden_slope, _ = np.polyfit(ref_data[:,0], ref_data[:,1], 1)
        else:
            # Fixed 0-70 Slope
            f0 = np.interp(0, ref_data[:,0], ref_data[:,1])
            f70 = np.interp(70, ref_data[:,0], ref_data[:,1])
            golden_slope = (f70 - f0) / 70.0

# ---- 2. Processing and Plotting ----
plt.figure(figsize=(14, 8))
corner_files = [f for f in all_files if "mm" not in f]
corner_colors = plt.cm.turbo(np.linspace(0, 1, len(corner_files)))

error_data_for_spread = []
temp_axis, mc_labeled, corner_idx = None, False, 0

for i, file_path in enumerate(all_files):
    data = parse_data(file_path)
    if data is None or len(data) == 0: continue
    
    if plot_mode == "0-70":
        mask = (data[:, 0] >= 0) & (data[:, 0] <= 70)
        data = data[mask]
        if len(data) == 0: continue

    x, y = data[:, 0], data[:, 1]
    if temp_axis is None: temp_axis = x
    
    # --- APPLY CALIBRATION & FIT LOGIC ---
    if cal_mode == "2-point":
        if fit_method == "best-fit":
            a, b = np.polyfit(x, y, 1)
        else:
            # Force zero error at 0 and 70 for this specific chip
            f0, f70 = np.interp(0, x, y), np.interp(70, x, y)
            a = (f70 - f0) / 70.0
            b = f0 # Because (a * 0) is 0
    else:
        # 1-Point Mode
        a = golden_slope
        b = np.mean(y - (a * x)) # Center the offset

    measured_temp = (y - b) / a
    error = measured_temp - x
    if len(error) == len(temp_axis): error_data_for_spread.append(error)
    
    # --- PLOTTING ---
    c_name = os.path.basename(file_path).replace("_oscillator.csv", "").replace("tran_LayGt", "")
    if "KttTtVt" in c_name and "mm" not in c_name:
        plt.plot(x, error, color='black', linewidth=4, zorder=99)
        plt.plot(x, error, color='red', linewidth=2.5, label="TYPICAL", zorder=100)
        corner_idx += 1
    elif "mm" in c_name:
        lbl = "Monte Carlo" if not mc_labeled else None
        plt.plot(x, error, color='gray', linewidth=0.8, alpha=0.3, zorder=1, label=lbl)
        mc_labeled = True
    else:
        plt.plot(x, error, color=corner_colors[corner_idx], linewidth=1.2, label=c_name, alpha=0.8, zorder=50)
        corner_idx += 1

# ---- 3. Formatting ----
if error_data_for_spread:
    all_errs = np.array(error_data_for_spread)
    plt.fill_between(temp_axis, np.max(all_errs, axis=0), np.min(all_errs, axis=0), color='blue', alpha=0.05)

plt.title(f"LPE Error: {cal_mode}, {fit_method} fit, {plot_mode} range", fontsize=14, fontweight='bold')
plt.xlabel("Actual Temperature (°C)", fontweight='bold'); plt.ylabel("Error (°C)", fontweight='bold')
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=6, fontsize='x-small', frameon=True)
plt.tight_layout()
plt.show()
