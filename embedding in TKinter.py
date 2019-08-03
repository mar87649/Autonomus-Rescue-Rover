import serial
from tkinter import *
import tkinter
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#====== VARIABLES ===========================================================

COM = "COM14" #COM port
BAUD = 9600   #Baudrate
forward = 'w' #move forward
reverse = 's' #move reverse
left    = 'a' #turn left
right   = 'd' #turn right
stop    = ' ' #stop movement
scan    = 'S' #do one scan
deliver = 'D' #do one delivery
mode_A  = '1' #automatic mode
mode_M  = '2' #manual mode
mode_P  = '3' #path follow mode
mode = 0
comand = 0

root = Tk() #========================================== Begining

#GUI definitions
def send_stop():
    ser.close()
    ser.open()
    ser.write(b' ')
    print("space")
    ser.close()
def send_forward():
    ser.close()
    ser.open()
    ser.write(b'w')
    print("sent w")
    ser.close()
def send_reverse():
    ser.close()
    ser.open()
    ser.write(b's')
    print("sent s")
    ser.close()
def send_left():
    ser.close()
    ser.open()
    ser.write(b'a')
    print("sent a")
    ser.close()
def send_right():
    ser.close()
    ser.open()
    ser.write(b'd')
    print("sent d")
    ser.close()
def send_scan():
    global comand
    comand = "S"
    ser.close()
    ser.open()
    ser.write(b'S')
    print("sent S")
    ser.close()
def send_deliver():
    ser.close()
    ser.open()
    ser.write(b'D')
    print("sent D")
    ser.close()
def send_mode_A():
    global mode
    ser.close()
    ser.open()
    mode = 1
    ser.write(b'1')
    print("sent 1")
    ser.close()
def send_mode_M():
    global mode
    ser.close()
    ser.open()
    mode = 2
    ser.write(b'2')
    print("sent 2")
    ser.close()
def send_mode_P():
    global mode
    ser.close()
    ser.open()
    mode = 3
    ser.write(b'3')
    print("sent 3")
    ser.close()
def Quit_App():
    root.quit()
    root.destroy()

# ======== CONTROL =============================================================
stop_button = tkinter.Button(master=root, text="stop", command=send_stop)
stop_button.grid(row=4, column=2)

forward_button = tkinter.Button(master=root, text="forward", command=send_forward)
forward_button.grid(row=1, column=2)

reverse_button = tkinter.Button(master=root, text="reverse", command=send_reverse)
reverse_button.grid(row=3, column=2)

left_button = tkinter.Button(master=root, text="left", command=send_left)
left_button.grid(row=2, column=0)

right_button = tkinter.Button(master=root, text="right", command=send_right)
right_button.grid(row=2, column=3)

scan_button = tkinter.Button(master=root, text="scan", command=send_scan)
scan_button.grid(row=2, column=6)

deliver_button = tkinter.Button(master=root, text="deliver", command=send_deliver)
deliver_button.grid(row=3, column=6)

#=========== modeS ==============================================

automatic_mode = tkinter.Button(master=root, text="automatic", command=send_mode_A)
automatic_mode.grid(row=2, column=8)

manual_mode = tkinter.Button(master=root, text="manual", command=send_mode_M)
manual_mode.grid(row=3, column=8)

path_mode = tkinter.Button(master=root, text="path follow", command=send_mode_P)
path_mode.grid(row=4, column=8)

#========= OTHER ===============================

Quit_button = tkinter.Button(master=root, text="Quit", command=Quit_App)
Quit_button.grid(row=5, column=2)

#====== SERIAL COM =======================================================================================

ser = serial.Serial(COM, BAUD)
ser.close()

#===========================================
count = 0
xdata = []
ydata = []

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
sc = ax1.scatter(xdata,ydata)
plt.xlim(-200,200)
plt.ylim(-200,200)

def print_data(count, dist, ang, x, y, xdata, ydata):
    print("count: ", count)
    print("distance: ", dist, "angle: ", ang)
    print("x-cord: ", x, ",", "y-cord: ",  y)
    print(xdata)
    print(ydata)
    print("")

def Scan():
    global count, xdata, ydata, mode
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

    sc.set_offsets(np.c_[xdata, ydata])

def animate(i):
    global count, xdata, ydata, mode, comand

    if (mode == 1):
        Scan()
    elif (mode ==2):
        if (comand == "S"):
            Scan()
            comand = 0



plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(row=0,column=0, columnspan=20)
ani = animation.FuncAnimation(fig, animate, interval=1, blit=False)

root.mainloop() #=========================================================== END



