import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0,10,0.1) 
x = np.arange(0,10,0.1)
y = np.arange(0,10,0.1)
z = np.arange(0,10,0.1)
tilt = np.arange(0,10,0.1)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, baudrate = 115200)
for i in range(0, 100):
    line=s.readline() 
    x[i] = float(line)
    line=s.readline() 
    y[i] = float(line)
    line=s.readline() 
    z[i] = float(line)
    line=s.readline() 
    tilt[i] = float(line)

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x)
ax[0].plot(t,y)
ax[0].plot(t,z)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(t,tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()