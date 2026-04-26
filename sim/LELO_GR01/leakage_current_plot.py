import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

# --- Configuration ---
data_dir = "output_tran/"
# Updated pattern for leakage files
file_pattern = "tran_Lay*_leakage.csv"

def parse_csv_data(filename):
    if not os.path.exists(filename):
        return None
    try:
        df = pd.read_csv(filename, sep=';', names=['temp', 'freq', 'current'], skipinitialspace=True)
        # CHANGED: Scale to nA (1e9) instead of uA, as leakage is much smaller
        df['current'] = pd.to_numeric(df['current'], errors='coerce') * 1e9
        df['temp'] = pd.to_numeric(df['temp'], errors='coerce')
        return df.dropna().sort_values(by='temp')
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return None

# ---- 1. Gather All Files ----
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))

# Separate Corners from Monte Carlo
corner_files = [f for f in all_files if "mm" not in f]
mc_files = [f for f in all_files if "mm" in f]

if not all_files:
    print(f"No files found in {data_dir} matching {file_pattern}")
    exit()

# ---- 2. Processing and Plotting ----
plt.figure(figsize=(14, 8))
corner_colors = plt.cm.turbo(np.linspace(0, 1, len(corner_files)))

current_data_for_spread = []
temp_axis = None
mc_labeled = False 

# First Pass: Monte Carlo
for file_path in mc_files:
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    current_data_for_spread.append(df['current'].values)
    label = "Monte Carlo" if not mc_labeled else None
    plt.plot(df['temp'], df['current'], color='gray', linewidth=0.8, alpha=0.2, zorder=1, label=label)
    mc_labeled = True

# Second Pass: Corners
color_idx = 0
for file_path in corner_files:
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    x, y = df['temp'].values, df['current'].values
    if temp_axis is None: temp_axis = x
    current_data_for_spread.append(y)
    
    # Updated replacement logic for leakage filename
    corner_name = os.path.basename(file_path).replace("_leakage.csv", "").replace("tran_LayGt", "")
    
    if "KttTtVt" in corner_name:
        plt.plot(x, y, color='black', linewidth=5, zorder=99) 
        plt.plot(x, y, color='red', linewidth=3, label="TYPICAL (KttTtVt)", zorder=100)
    else:
        plt.plot(x, y, color=corner_colors[color_idx], linestyle='-', linewidth=1.8, label=corner_name, zorder=50)
        color_idx += 1

# ---- 3. Spread Area ----
if current_data_for_spread:
    min_len = min(len(arr) for arr in current_data_for_spread)
    clipped_data = np.array([arr[:min_len] for arr in current_data_for_spread])
    final_temp = temp_axis[:min_len] if temp_axis is not None else np.arange(min_len)

    y_max = np.max(clipped_data, axis=0)
    y_min = np.min(clipped_data, axis=0)
    plt.fill_between(final_temp, y_max, y_min, color='blue', alpha=0.05, label="Total Leakage Spread", zorder=2)

# ---- 4. Formatting ----
plt.yscale('log') # IMPORTANT: Leakage is exponential, log scale is usually better
plt.xlabel("Temperature (°C)", fontsize=12, fontweight='bold')
plt.ylabel("Leakage Current Consumption (nA)", fontsize=12, fontweight='bold')
plt.title("LPE Leakage Current: Process Corners & Monte Carlo", fontsize=14, fontweight='bold')
plt.grid(True, which='both', linestyle=':', alpha=0.6)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5, fontsize='small', frameon=True, shadow=True)

plt.tight_layout()
plt.savefig("leakage_analysis.png", dpi=300)
print(f"Finished: {len(corner_files)} corners and {len(mc_files)} Monte Carlo runs processed.")
plt.show()
