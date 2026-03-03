#Read the frequency measurements of the oscillator at different frequencies from different csv files and plot the errors of temperature measurements


import numpy as np
import matplotlib.pyplot as plt


measurement_time = 1/32768             #Slice time in which we count the oscillations to measure frequency



def parse_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().split("\n")

    measurements = []
    for i in range(len(lines)):
        line_split = lines[i].split(";")
        if len(line_split) == 2:
            measurements.append([float(line_split[0]), float(line_split[1])]) 

    return np.array(measurements)



data_files = ["tran_SchGtKssTtVl", "tran_SchGtKttTlVt", "tran_SchGtKffTlVt"]
#data_files = ["../data"]

measurements_list = []
for file in data_files:
    measurements_list.append(parse_data("output_tran/"+file+".csv"))



#---- Compute the linear regression of the mesurements ----#
a_list = []
b_list = []
for i in range(len(measurements_list)):
    a, b = np.polyfit(measurements_list[i][:, 0], measurements_list[i][:, 1], 1)
    a_list.append(a)
    b_list.append(b)




#---- Plotting the linear regression and the measurements ----#
plt.figure()
for i in range(len(measurements_list)):
    x_line = np.linspace(measurements_list[i][:, 0].min(), measurements_list[i][:, 0].max(), 10)
    y_line = a_list[i] * x_line + b_list[i]
    plt.scatter(measurements_list[i][:, 0], measurements_list[i][:, 1], label=data_files[i])
    plt.plot(x_line, y_line)

plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency (Hz)")
plt.title("Frequency measurements")
plt.legend()
plt.grid(True)







#---- Computing measurements errors ----#
measured_temperature_error_list = []
for i in range(len(measurements_list)):
    measured_temperature = (measurements_list[i][:, 1]-b_list[i])/a_list[i]
    measured_temperature_error_list.append(measured_temperature - measurements_list[i][:, 0])




#---- Computing for each temperature the max and min error ----#
y_max = []
y_min = []
for i in range(len(measurements_list[0][:, 0])):
    y_max.append(measured_temperature_error_list[0][i])
    y_min.append(measured_temperature_error_list[0][i])
    for j in range(len(measured_temperature_error_list)):
        if y_max[-1] < measured_temperature_error_list[j][i]:
            y_max[-1] = measured_temperature_error_list[j][i]
        if y_min[-1] > measured_temperature_error_list[j][i]:
            y_min[-1] = measured_temperature_error_list[j][i]




#---- Plotting the measured temperature error ----#
PLOT_ONLY_TYPICAL=True #Assuming that typical is the the data_files list
plt.figure()
plt.fill_between(measurements_list[0][:, 0], y_max, y_min, alpha=0.3, label="Area where all the measurements fit in")

if PLOT_ONLY_TYPICAL:
    plt.plot(measurements_list[0][:, 0], measured_temperature_error_list[i], label=data_files[i], marker='o')
else:
    for i in range(len(measurements_list)):
        plt.plot(measurements_list[i][:, 0], measured_temperature_error_list[i], label=data_files[i], marker='o')


plt.xlabel("Temperature (°C)")
plt.ylabel("Temperature measurements error (°C)")
plt.title("Temperature measurements error")
plt.legend()
plt.grid(True)




'''
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

'''




plt.show()
