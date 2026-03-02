#Read the frequency measurements of the oscillator at different frequencies from the files oscillator.csv and plot the linearity errors


import numpy as np
import matplotlib.pyplot as plt


filename = "data.csv"  #data file
measurement_time = 1/32768             #Slice time in which we count the oscillations to measure frequency



def parse_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().split("\n")


    measurements = []
    for i in range(1, len(lines)):
        line_split = lines[i].split(";")
        if len(line_split) == 2:
            measurements.append([float(line_split[0]), float(line_split[1])])

    measurements  = np.array(measurements)

    return measurements







measurements = parse_data(filename)
x = measurements[:, 0]
y = measurements[:, 1]


#---- Compute the linear regression of the mesurements ----#
a, b = np.polyfit(x, y, 1)



#---- Plotting the linear regression and the measurements ----#
x_line = np.linspace(x.min(), x.max(), 10)
y_line = a * x_line + b
plt.figure()
plt.scatter(x, y, color="blue", label="Measured frequency")
plt.plot(x_line, y_line, color="red", label=f"y = {a:.2f}x + {b:.2f}")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency (Hz)")
plt.title("Frequency measurements")
plt.legend()
plt.grid(True)



#---- Plotting the measured temperature error ----#
measured_temperature = (y-b)/a
measured_temperature_error = measured_temperature - x
plt.figure()
plt.plot(x, measured_temperature_error, color="blue", label="error", marker='o')
plt.xlabel("Temperature (°C)")
plt.ylabel("Temperature measurements error (°C)")
plt.title("Temperature measurements error")
plt.legend()
plt.grid(True)


#---- Plotting the measured temperature error without and with the quantification noise ----#
number_oscillations = (measurement_time * y).astype(int)    #Number of oscillations that occur during the measurement time
a_q, b_q = np.polyfit(x, number_oscillations, 1)            #Compute a new linear regression with a quantified number of oscillations
measured_temperature_q = (number_oscillations-b_q)/a_q
measured_temperature_error_q = measured_temperature_q - x
plt.figure()
plt.plot(x, measured_temperature_error_q, color="blue", label="error with quantification noise", marker='o')
plt.plot(x, measured_temperature_error, color="red", label="error without quantification noise", marker='o')
plt.xlabel("Temperature (°C)")
plt.ylabel("Temperature measurements error (°C)")
plt.title("Temperature estimation error")
plt.legend()
plt.grid(True)






plt.show()

#print(measurements)