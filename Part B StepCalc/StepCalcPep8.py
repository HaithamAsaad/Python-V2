# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:55:00 2018

@author: haitham
"""
# importing important libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal


# define a function for square calculation
def square(list):
    return [i ** 2 for i in list]


# define a function for square root calculation
def sqrtList(list):
    return [j ** (1/2) for j in list]

# Load the xls data, and use Sheet3
loc = "C:/Users/haithama/Desktop/KPIT training presentations/Python/\
20180723_12_27_32_data.xls"
file = pd.ExcelFile(loc)
file.sheet_names
df = file.parse('Sheet3')

# Extract the acceleration data and save them to seperate lists
accX = df['user_acc_x(G)']
accY = df['user_acc_y(G)']
accZ = df['user_acc_z(G)']

# Plot acceleration into X dir
plt.plot(accX)
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Acceleration in X dir')
plt.legend()
plt.show()

# Plot acceleration into Y dir
plt.plot(accY)
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Acceleration in Y dir')
plt.legend()
plt.show()

# Plot acceleration into Z dir
plt.plot(accZ)
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Acceleration in Z dir')
plt.legend()
plt.show()
# determining the magnitude of the acceleration data in 3 axises
accT = list(np.array(square(accX)) + np.array(square(accY)) + np.array(square(accY)))  # noqa
Mag = sqrtList(accT)
# plot the magnitude
plt.plot(Mag, 'g')
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Acceleration data magnitude')
plt.legend()
plt.show()

# finding the number of steps
peakind = signal.find_peaks_cwt(Mag, np.arange(1, len(Mag)))

print("Number of steps = ", len(peakind))
