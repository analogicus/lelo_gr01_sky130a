import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import random
from itertools import cycle

# --- Configuration ---
data_dir = "final_results/sch/csv" 
file_pattern = "tran_*_oscillator.csv"

# --- TOGGLES ---
plot_mode = "full"   
cal_mode = "2-point" 
fit_method = "fixed" 
omit_corners = ["None"] 

# --- Reference Corner for Golden Slope ---
reference_corner = "Ktt"

# ---- 0. Determine Plot Title ----
sim_type = "Schematic-Based (Pre-LPE)" if "/sch/" in data_dir.lower() else "Layout-Based (LPE)"

def parse_data(filename):
    measurements = []
    if not os.path.exists(filename): return np.empty((0, 2))
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line_split = line.split(";")
        if len(line_split) >= 2: 
            try:
                measurements.append([float(line_split[0]), float(line_split[1])])
            except ValueError: continue
    res = np.array(measurements)
    return res if res.ndim == 2 else res.reshape(-1, 2) if res.size > 0 else np.empty((0, 2))

# ---- 1. Gather and Filter Files ----
all_files = sorted(glob.glob(os.path.join(data_dir, file_pattern)))
if omit_corners and "None" not in omit_corners:
    all_files = [f for f in all_files if not any(omit in os.path.basename(f) for omit in omit_corners)]

filtered_files = [f for f in all_files if ("KttTtVt" in f and "mm" not in f) or ("mm" in f) or 
                  (any(c in f for c in ["Kff", "Kfs", "Ksf", "Kss"]) and ("ThVh" in f or "ThVl" in f))]

# ---- 2. Slope Calculation ----
golden_slope = 1.0
if cal_mode == "1-point":
    ref_file = next((f for f in filtered_files if reference_corner in f and "mm" not in f), None)
    if not ref_file:
        ref_file = next((f for f in filtered_files if "KttTtVt" in f), None)
        print(f"Warning: {reference_corner} not found. Falling back to Ktt for slope.")

    if ref_file:
        ref_data = parse_data(ref_file)
        if ref_data.shape[0] > 1:
            if fit_method == "best-fit":
                golden_slope, _ = np.polyfit(ref_data[:,0], ref_data[:,1], 1)
            else:
                f25_ref = np.interp(25, ref_data[:,0], ref_data[:,1])
                f85_ref = np.interp(85, ref_data[:,0], ref_data[:,1])
                golden_slope = (f85_ref - f25_ref) / 60.0
            if abs(golden_slope) < 1e-12: golden_slope = 1.0

# ---- 3. Processing ----
processed_results, max_delta, worst_trace_info = [], -1, {}
Y_VIEW_LIMIT = 20

for file_path in filtered_files:
    data = parse_data(file_path)
    if data.size < 4: continue 
    x_f, y_f = data[:, 0], data[:, 1]
    
    if cal_mode == "2-point":
        if fit_method == "best-fit":
            a, b = np.polyfit(x_f, y_f, 1)
        else:
            f25, f85 = np.interp(25, x_f, y_f), np.interp(85, x_f, y_f)
            a = (f85 - f25) / 60.0
            b = f25 - (a * 25.0)
    else: # 1-point
        a = golden_slope
        if fit_method == "best-fit":
            b = np.mean(y_f - (a * x_f))
        else:
            f25_local = np.interp(25, x_f, y_f)
            b = f25_local - (a * 25.0)

    err_f = ((y_f - b) / a) - x_f
    
    t_win = np.sort(np.unique(np.concatenate([x_f[(x_f >= 0) & (x_f <= 70)], [0.0, 70.0]])))
    e_win = np.interp(t_win, x_f, err_f)
    d = np.max(e_win) - np.min(e_win)
    
    if d > max_delta:
        max_delta = d
        worst_trace_info = {'name': os.path.basename(file_path), 't_max': t_win[np.argmax(e_win)], 
                            'v_max': np.max(e_win), 't_min': t_win[np.argmin(e_win)], 
                            'v_min': np.min(e_win), 'delta': d}

    processed_results.append({'name': os.path.basename(file_path), 'x': x_f, 'err': err_f,
                              'is_typ': "KttTtVt" in file_path and "mm" not in file_path,
                              'is_mc': "mm" in file_path})

# ---- 4. Plotting ----
plt.figure(figsize=(15, 9))
color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
color_cycle = cycle(color_palette)
mc_labeled = False

for res in processed_results:
    x, err = res['x'], res['err']
    if plot_mode == "0-70":
        mask = (x >= -2) & (x <= 72)
        x, err = x[mask], err[mask]
    if len(x) == 0: continue

    if res['is_typ']:
        plt.plot(x, err, color='red', lw=3, label="TYPICAL", zorder=100)
    elif res['is_mc']:
        plt.plot(x, err, color='dimgray', lw=0.5, alpha=0.1, zorder=1, label="Monte Carlo" if not mc_labeled else "")
        mc_labeled = True
    else:
        is_worst = (res['name'] == worst_trace_info.get('name'))
        plt.plot(x, err, color='#00CED1' if is_worst else next(color_cycle), 
                 lw=3.5 if is_worst else 1.2, ls='-' if is_worst else '--', 
                 label=f"{res['name']} {'(WORST)' if is_worst else ''}", 
                 zorder=150 if is_worst else 50)

# ---- 5. Visual Elements & Annotations ----
if worst_trace_info:
    wi = worst_trace_info
    bx = 70 if plot_mode == "0-70" else 75
    v_max_c = np.clip(wi['v_max'], -Y_VIEW_LIMIT, Y_VIEW_LIMIT)
    v_min_c = np.clip(wi['v_min'], -Y_VIEW_LIMIT, Y_VIEW_LIMIT)
    
    plt.hlines([v_max_c, v_min_c], [wi['t_max'], wi['t_min']], bx, colors='darkred', ls=':', lw=1.2)
    plt.vlines(bx, v_min_c, v_max_c, colors='darkred', lw=3, zorder=160)

    txt = (f"MAX DELTA (0-70°C): {wi['delta']:.3f}°C\n"
           f"Peak: {wi['v_max']:.3f}°C / Min: {wi['v_min']:.3f}°C\n"
           f"Corner: {wi['name']}\nRef Slope: {reference_corner}")
    
    plt.annotate(txt, xy=(bx, (v_max_c + v_min_c)/2), xytext=(0.98, 0.7),
                 textcoords='axes fraction', ha='right',
                 arrowprops=dict(arrowstyle='->', color='darkred', connectionstyle="arc3,rad=-0.1"),
                 bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="darkred", alpha=0.9),
                 fontsize=9, fontweight='bold', zorder=200)

plt.axvspan(0, 70, color='gold', alpha=0.15, label='0-70°C Window') 
plt.axhline(0, color='black', lw=1.2); plt.grid(True, alpha=0.2)

# --- DYNAMIC SPEC LINES ---
spec_val = 5 if cal_mode == "2-point" else 10
plt.axhline(spec_val, color='red', ls=':', lw=2, alpha=0.7, label=f'Spec ±{spec_val}°C')
plt.axhline(-spec_val, color='red', ls=':', lw=2, alpha=0.7)

plt.title(f"{sim_type}\nRef Slope: {reference_corner} | Cal: {cal_mode} | Range: {plot_mode}", fontsize=14, fontweight='bold')
plt.xlabel("Temperature (°C)", fontweight='bold'); plt.ylabel("Error (°C)", fontweight='bold')

plt.ylim(-Y_VIEW_LIMIT, Y_VIEW_LIMIT)
if plot_mode == "0-70": plt.xlim(-5, 75)
else: plt.xlim(-45, 130)

n_entries = len(plt.gca().get_legend_handles_labels()[1])
n_cols = min(4, n_entries)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), 
           ncol=n_cols, fontsize='7', frameon=True, borderaxespad=0.)

plt.tight_layout()
plt.subplots_adjust(bottom=0.2) 
plt.show()
