import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

# --- Configuration ---
data_dir = "output_tran/" 
file_pattern = "tran_Lay*_oscillator.csv"

def parse_csv_data(filename):
    if not os.path.exists(filename):
        return None
    try:
        df = pd.read_csv(filename, sep=';', names=['temp', 'freq', 'current'], skipinitialspace=True)
        # Convert to float and scale to uA
        df['current'] = pd.to_numeric(df['current'], errors='coerce') * 1e6
        df['temp'] = pd.to_numeric(df['temp'], errors='coerce')
        return df.dropna().sort_values(by='temp')
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return None

# ---- 1. Gather All Files ----
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))

# Separate Corners from Monte Carlo to define the colormap only for corners
corner_files = [f for f in all_files if "mm" not in f]
mc_files = [f for f in all_files if "mm" in f]

if not all_files:
    print(f"No files found in {data_dir} matching {file_pattern}")
    exit()

# ---- 2. Processing and Plotting ----
plt.figure(figsize=(14, 8))

# 'turbo' or 'brg' are highly distinct colormaps for many lines
corner_colors = plt.cm.turbo(np.linspace(0, 1, len(corner_files)))

current_data_for_spread = []
temp_axis = None
mc_labeled = False 

# First Pass: Plot Monte Carlo (so they sit in the background)
for file_path in mc_files:
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    current_data_for_spread.append(df['current'].values)
    label = "Monte Carlo" if not mc_labeled else None
    
    # Increased alpha to 0.3 and width to 0.8 for better visibility
    plt.plot(df['temp'], df['current'], color='gray', linewidth=0.8, alpha=0.3, zorder=1, label=label)
    mc_labeled = True

# Second Pass: Plot Corners
color_idx = 0
for file_path in corner_files:
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    x, y = df['temp'].values, df['current'].values
    if temp_axis is None: temp_axis = x
    current_data_for_spread.append(y)
    
    corner_name = os.path.basename(file_path).replace("_oscillator.csv", "").replace("tran_LayGt", "")
    
    if "KttTtVt" in corner_name:
        # TYPICAL: Thick Black outline with Red center for maximum contrast
        plt.plot(x, y, color='black', linewidth=5, zorder=99) 
        plt.plot(x, y, color='red', linewidth=3, label="TYPICAL (KttTtVt)", zorder=100)
    else:
        # CORNERS: Highly distinct colors
        plt.plot(x, y, color=corner_colors[color_idx], linestyle='-', linewidth=1.8, label=corner_name, zorder=50)
        color_idx += 1

# ---- 3. Spread Area (Min/Max Envelope) ----
if current_data_for_spread:
    # Handle potentially different simulation lengths
    min_len = min(len(arr) for arr in current_data_for_spread)
    clipped_data = np.array([arr[:min_len] for arr in current_data_for_spread])
    
    # We use the temperature axis from the first valid file
    final_temp = temp_axis[:min_len] if temp_axis is not None else np.arange(min_len)

    y_max = np.max(clipped_data, axis=0)
    y_min = np.min(clipped_data, axis=0)
    plt.fill_between(final_temp, y_max, y_min, color='blue', alpha=0.05, label="Total Spread Envelope", zorder=2)

# ---- 4. Formatting ----
plt.xlabel("Temperature (°C)", fontsize=12, fontweight='bold')
plt.ylabel("Average Current Consumption (µA)", fontsize=12, fontweight='bold')
plt.title("LPE Active Current Consumption: Process Corners & Monte Carlo", fontsize=14, fontweight='bold')
plt.grid(True, which='both', linestyle=':', alpha=0.6)

# Legend formatting
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5, fontsize='small', frameon=True, shadow=True)

plt.tight_layout()
plt.savefig("current_analysis_v2.png", dpi=300)
print(f"Finished: {len(corner_files)} corners and {len(mc_files)} Monte Carlo runs processed.")
plt.show()
