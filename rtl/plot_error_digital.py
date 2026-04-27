#Read the frequency measurements of the oscillator at different frequencies from different csv files and plot the errors of temperature measurements


import numpy as np
import matplotlib.pyplot as plt


def parse_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().split("\n")

    measurements = []
    for i in range(1,len(lines)):
        line_split = lines[i].split(";")
        if len(line_split) == 2:
            measurements.append([float(line_split[0]), float(line_split[1])]) 

    return np.array(measurements)





filename = "rtl.csv"
measurements = parse_data(filename)

x = measurements[:,0]
y = measurements[:,1]

print(y)





#---- Compute the linear regression of the mesurements ----#

count25 = np.interp(25, x, y)
count85 = np.interp(85, x, y)

a = (count85-count25) / (85.0 - 25.0) #Slope of the linear regression
b = count25 - 25.0*a

print(count25)



fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # 1 ligne, 2 colonnes


#---- Plotting the linear regression and the measurements ----#
#plt.figure()

axs[0].scatter(x, y, label="Ouput value of the FSM") #Measurements

x_line = np.linspace(x.min(), x.max(), 10) #Linear regression
y_line = a * x_line + b
axs[0].plot(x_line, y_line, color="red", label="Linear regression with 2 points\ncalibration (25°C - 85°C)")
    

axs[0].set_xlabel("Temperature (°C)")
axs[0].set_ylabel("Output value (in number of pulses from the oscillator)")
axs[0].set_title("Output value of the FSM in function of temperature,\nfor typical LPE run")
axs[0].legend()
axs[0].grid(True)






#---- Computing measurements errors ----#

measured_temperature = (y-b)/a
measured_temperature_error = measured_temperature - x

#plt.figure()
axs[1].plot(x, measured_temperature_error, label="Measurement error (°C)", marker='o')
axs[1].scatter([25, 85], [0, 0], color='red', zorder=3, label="Calibration points")
axs[1].axhline(y=0, color='black')
axs[1].set_xlabel("Temperature (°C)")
axs[1].set_ylabel("Temperature measurement error (°C)")
axs[1].set_title("Digital temperature measurement error,\nfor typical LPE run and two points calibration (25°C - 85°C)")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()

exit()