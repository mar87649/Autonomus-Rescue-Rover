from tkinter import *
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
#==================================================

#==================================================
root = Tk()
# ================== MAP FRAME =====================
map_frame = Frame(root)
map_frame.pack(side=RIGHT)

fig, ax = plt.subplots()
fig2 = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
canvas.draw()

xdata = []
ydata = []
sc = ax.scatter(xdata, ydata)
plt.xlim(-200, 200)
plt.ylim(-200, 200)

def animate(i):

    global count, xdata, ydata
    xdata = np.append(xdata, np.random.randint(200, size=1))
    ydata = np.append(ydata, np.random.randint(200, size=1))
    sc.set_offsets(np.c_[xdata, ydata])



ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=2, interval=100, repeat=True)

plot.draw()
# ================== INFO FRAME =====================
info_frame = Frame(root)
info_frame.pack(side = BOTTOM)
# ================== CONTROL FRAME =====================
control_frame = Frame(root)
control_frame.pack(side = LEFT)


root.mainloop()