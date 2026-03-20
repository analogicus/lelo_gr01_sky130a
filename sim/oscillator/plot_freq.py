import csv
import matplotlib.pyplot as plt

temps = []
freqs = []

with open("output_tran/oscillator.csv") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)  # skip header
    for row in reader:
        temps.append(float(row[0].strip()))
        freqs.append(float(row[1].strip()) / 1e6)

plt.figure()
plt.plot(temps, freqs, "o-")
plt.xlabel("Temperature [°C]")
plt.ylabel("Frequency [MHz]")
plt.title("Oscillator Frequency vs Temperature")
plt.grid(True)
plt.tight_layout()
plt.savefig("output_tran/oscillator_freq.png", dpi=150)
plt.show()
