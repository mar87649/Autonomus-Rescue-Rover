import serial
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()

xdata = []
ydata = []

fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 100)
line, = ax1.plot(xdata, ydata, 'bo')
m
def animate(i):
    ydata.append(99-i)
    xdata.append(i)
    line.set_data(xdata, ydata)
    ax1.set_xlim(0, i+1)

plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(column=1, row=1)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)

root.mainloop()