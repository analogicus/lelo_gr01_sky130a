import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

# --- Configuration ---
data_dir = "final_results/sch_leak/csv/"
file_pattern = "tran_*_leakage.csv"

def parse_csv_data(filename):
    if not os.path.exists(filename):
        return None
    try:
        df = pd.read_csv(filename, sep=';', names=['temp', 'freq', 'current'], skipinitialspace=True)
        # Scale to nA (1e9)
        df['current'] = pd.to_numeric(df['current'], errors='coerce') * 1e9
        df['temp'] = pd.to_numeric(df['temp'], errors='coerce')
        return df.dropna().sort_values(by='temp')
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return None

# ---- 1. Gather All Files ----
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))
corner_files = [f for f in all_files if "mm" not in f]
mc_files = [f for f in all_files if "mm" in f]

if not all_files:
    print(f"No files found in {data_dir} matching {file_pattern}")
    exit()

# ---- 2. Processing and Plotting ----
plt.figure(figsize=(14, 8))
# Use len(corner_files) to ensure color array matches file count
corner_colors = plt.cm.turbo(np.linspace(0, 1, len(corner_files)))

current_data_for_spread = []
temp_axis = None
mc_labeled = False 
val_at_25_nA = None

# First Pass: Monte Carlo
for file_path in mc_files:
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    current_data_for_spread.append(df['current'].values)
    label = "Monte Carlo" if not mc_labeled else None
    plt.plot(df['temp'], df['current'], color='gray', linewidth=0.8, alpha=0.2, zorder=1, label=label)
    mc_labeled = True

# Second Pass: Corners
for color_idx, file_path in enumerate(corner_files):
    df = parse_csv_data(file_path)
    if df is None or df.empty: continue
    
    x, y = df['temp'].values, df['current'].values
    if temp_axis is None: temp_axis = x
    current_data_for_spread.append(y)
    
    # Robust corner name cleaning
    corner_name = os.path.basename(file_path).replace("_leakage.csv", "").replace("tran_LayGt", "").replace("tran_SchGt", "")
    
    if "KttTtVt" in corner_name:
        plt.plot(x, y, color='black', linewidth=5, zorder=99) 
        plt.plot(x, y, color='red', linewidth=3, label="TYPICAL (KttTtVt)", zorder=100)
        
        # --- MATH: Log-Linear Interpolation for 25C ---
        # Interpolate in log-domain because leakage is exponential
        log_y = np.log(y)
        log_val_at_25 = np.interp(25, x, log_y)
        val_at_25_nA = np.exp(log_val_at_25)
    else:
        plt.plot(x, y, color=corner_colors[color_idx], linestyle='-', linewidth=1.8, label=corner_name, zorder=50)

# ---- 3. Annotation: Log-Interpolated Typical @ 25C ----
if val_at_25_nA is not None:
    plt.annotate(f'Typical @ 25°C: {val_at_25_nA:.4f} nA',
                 xy=(25, val_at_25_nA),
                 xytext=(5, val_at_25_nA * 10), # Offset text above the point
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
                 fontsize=11, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.9),
                 zorder=150)
    # Visual marker for the exact calculated point
    plt.scatter(25, val_at_25_nA, color='yellow', edgecolor='black', s=150, marker='*', zorder=101, label="Calculated 25°C Point")

# ---- 4. Spread Area ----
if current_data_for_spread:
    min_len = min(len(arr) for arr in current_data_for_spread)
    clipped_data = np.array([arr[:min_len] for arr in current_data_for_spread])
    final_temp = temp_axis[:min_len] if temp_axis is not None else np.arange(min_len)

    y_max = np.max(clipped_data, axis=0)
    y_min = np.min(clipped_data, axis=0)
    plt.fill_between(final_temp, y_max, y_min, color='blue', alpha=0.05, label="Total Leakage Spread", zorder=2)

# ---- 5. Formatting ----
plt.yscale('log')
plt.xlabel("Temperature (°C)", fontsize=12, fontweight='bold')
plt.ylabel("Leakage Current Consumption (nA)", fontsize=12, fontweight='bold')
plt.title("SCH Leakage Current: Process Corners & Monte Carlo", fontsize=14, fontweight='bold')
plt.grid(True, which='both', linestyle=':', alpha=0.6)

# Legend logic: ncol=4 or 5 depending on preference
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, fontsize='small', frameon=True, shadow=True)

plt.tight_layout()
plt.savefig("leakage_analysis.png", dpi=300)
print(f"Finished: {len(corner_files)} corners and {len(mc_files)} Monte Carlo runs processed.")
print(f"Typical Leakage @ 25°C (Calculated): {val_at_25_nA:.4f} nA")
plt.show()
