#Read the frequency measurements of the oscillator at different frequencies from different csv files and plot the errors of temperature measurements


import numpy as np
import matplotlib.pyplot as plt


measurement_time = 1/32768             #Slice time in which we count the oscillations to measure frequency



def parse_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().split("\n")

    measurements = []
    for i in range(1,len(lines)):
        line_split = lines[i].split(";")
        if len(line_split) == 2:
            measurements.append([float(line_split[0]), float(line_split[1])]) 

    return np.array(measurements)



#data_files = ["tran_SchGtKssTtVl", "tran_SchGtKttTlVt", "tran_SchGtKffTlVt"]
#data_files = ["../data"]



#remove

data_files = ['oscillator_typical_reduce',
    # 'etc/tran_SchGtKssTlVh_oscillator', 'etc/tran_SchGtKsfTlVh_oscillator', 'etc/tran_SchGtKfsTlVh_oscillator', 'etc/tran_SchGtKfsThVh_oscillator', 'etc/tran_SchGtKssTlVl_oscillator', 'etc/tran_SchGtKssThVh_oscillator', 'etc/tran_SchGtKsfThVh_oscillator', 'etc/tran_SchGtKfsThVl_oscillator', 'etc/tran_SchGtKffTlVl_oscillator', 'etc/tran_SchGtKffThVh_oscillator', 'etc/tran_SchGtKffTlVh_oscillator', 'etc/tran_SchGtKsfTlVl_oscillator', 'etc/tran_SchGtKsfThVl_oscillator', 'etc/tran_SchGtKssThVl_oscillator', 'etc/tran_SchGtKfsTlVl_oscillator',
'mc/tran_SchGtKttmmTtVt_oscillator', 'mc/tran_SchGtKttmmTtVt_1_oscillator', 'mc/tran_SchGtKttmmTtVt_16_oscillator', 'mc/tran_SchGtKttmmTtVt_19_oscillator', 'mc/tran_SchGtKttmmTtVt_9_oscillator', 'mc/tran_SchGtKttmmTtVt_3_oscillator', 'mc/tran_SchGtKttmmTtVt_11_oscillator', 'mc/tran_SchGtKttmmTtVt_13_oscillator', 'mc/tran_SchGtKttmmTtVt_15_oscillator', 'mc/tran_SchGtKttmmTtVt_25_oscillator', 'mc/tran_SchGtKttmmTtVt_8_oscillator', 'mc/tran_SchGtKttmmTtVt_18_oscillator', 'mc/tran_SchGtKttmmTtVt_28_oscillator', 'mc/tran_SchGtKttmmTtVt_6_oscillator', 'mc/tran_SchGtKttmmTtVt_21_oscillator', 'mc/tran_SchGtKttmmTtVt_2_oscillator', 'mc/tran_SchGtKttmmTtVt_4_oscillator', 'mc/tran_SchGtKttmmTtVt_17_oscillator', 'mc/tran_SchGtKttmmTtVt_14_oscillator', 'mc/tran_SchGtKttmmTtVt_23_oscillator', 'mc/tran_SchGtKttmmTtVt_22_oscillator', 'mc/tran_SchGtKttmmTtVt_29_oscillator', 'mc/tran_SchGtKttmmTtVt_7_oscillator', 'mc/tran_SchGtKttmmTtVt_24_oscillator', 'mc/tran_SchGtKttmmTtVt_27_oscillator', 'mc/tran_SchGtKttmmTtVt_5_oscillator', 'mc/tran_SchGtKttmmTtVt_26_oscillator', 'mc/tran_SchGtKttmmTtVt_10_oscillator', 'mc/tran_SchGtKttmmTtVt_20_oscillator'
]


measurements_list = []
for file in data_files:
    measurements_list.append(parse_data("results_03.03.2026/"+file+".csv"))



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
    plt.scatter(measurements_list[i][:, 0], measurements_list[i][:, 1])
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
PLOT_ONLY_TYPICAL=False #Assuming that typical is the the data_files list
plt.figure()
plt.fill_between(measurements_list[0][:, 0], y_max, y_min, alpha=0.3, label="Area where all the measurements fit in")

if PLOT_ONLY_TYPICAL:
    plt.plot(measurements_list[0][:, 0], measured_temperature_error_list[i], label=data_files[i], marker='o')
else:
    for i in range(len(measurements_list)):
        plt.plot(measurements_list[i][:, 0], measured_temperature_error_list[i], marker='o')


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
