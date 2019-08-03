import serial

COM = "COM14"
BAUD = 9600
ser = serial.Serial(COM, BAUD)
ser.close()

ser.open()
dist = ord(ser.read())
ang = ord(ser.read())
ser.close()

#============================================
import time
import numpy as np

rad = np.deg2rad(ang)
x = np.cos(rad) * dist
y = np.sin(rad) * dist

#========================================

# xdata = []
# ydata = []
#
# def update(xdata, ydata):
#     xdata = np.append(xdata, x)
#     ydata = np.append(ydata, y)

#========================================
import matplotlib.pyplot as plt

count = 0

# while 1:
#     ser.open()
#     dist = ord(ser.read())
#     ang = ord(ser.read())
#     ser.close()
#
#     rad = np.deg2rad(ang)
#     x = np.cos(rad) * dist
#     y = np.sin(rad) * dist
#
#     x = int(round(x))
#     y = int(round(y))
#
#     update()
#     count = count + 1
#     print("count: ", count)
#     print("distance: ", dist, "angle: ", ang)
#     print("x-cord: ", x, ",", "y-cord: ",  y)
#     print("")
#     time.sleep(1)

    # if (count == 10):
    #     #print(xdata)
    #     print(ydata)
    #     plt.scatter(xdata, ydata)
    #     plt.show()
    #     break

#=================================================

def print_data(count, dist, ang, x, y, xdata, ydata):
    print("count: ", count)
    print("distance: ", dist, "angle: ", ang)
    print("x-cord: ", x, ",", "y-cord: ",  y)
    print(xdata)
    print(ydata)
    print("")

import matplotlib.animation

fig, ax = plt.subplots()
# fig = plt.figure()
# ax = fig.add_subplot(111)
xdata = []
ydata = []
sc = ax.scatter(xdata,ydata)
plt.xlim(-200,200)
plt.ylim(-200,200)

def animate(i):
    global count, xdata, ydata

    ser.open()
    dist = ord(ser.read())
    ang = ord(ser.read())
    ser.close()

    rad = np.deg2rad(ang)
    x = np.cos(rad) * dist
    y = np.sin(rad) * dist

    x = int(round(x))
    y = int(round(y))

    xdata = np.append(xdata, x)
    ydata = np.append(ydata, y)

    count = count + 1
    print_data(count, dist, ang, x, y, xdata, ydata)
    #time.sleep(1)

    sc.set_offsets(np.c_[xdata, ydata])



ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=None, interval=1, repeat=True)
plt.show()



