#Plot the counter value in function of the oscillator frequency

import os
import re
import subprocess
import time
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

#csv_data = "frequency (Hz) ; counter_value\n"
counter_values = []
freqs = range(1_700_000, 2_800_000, 5_000)
for f in tqdm(freqs):
    
    command_result = os.system("iverilog -g2012 -o sim.out -Ptestbench.OSC_FREQ="+str(f)+" test_LELO_TEMP.sv LELO_TEMP.sv")
    command_result = subprocess.run(["vvp", "sim.out"], capture_output=True, text=True).stdout
    match = re.search(r"Final out value = (\d+)", command_result)
    out = int(match.group(1))
    #csv_data += str(f)+" ; "+str(out)+"\n"
    counter_values.append(out)

'''
with open("counter_data.csv", 'w') as f:
    f.write(csv_data)
print(csv_data)'''

x = np.array(freqs, dtype=float)
y = np.array(counter_values, dtype=float)


#Linear regression forced to go through the origin
a = np.sum(x * y) / np.sum(x**2)
y_fit = a * x

# Plot
plt.figure()
plt.plot(x, y, label="Counter output")
plt.plot(x, y_fit, label=rf"Linear regression: $y = \frac{{1}}{{{round(1/a,2)}}}x$", color="red")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Counter value")
plt.title("Counter output in function of input frequency")
plt.legend()
plt.grid()

plt.show()



