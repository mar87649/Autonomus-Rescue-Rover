from PyQt5 import QtGui, QtCore  # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np
import serial
import numpy as np
from pyqtgraph.ptime import time
import sys




## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

p = pg.plot()
curve = p.plot()


xdata = [0]
ydata = [0]

ser = serial.Serial("COM11", 9600)

def update():
    global curve, xdata,ydata
    line = ser.readline()
    xdata.append(np.random.normal())
    ydata.append(int(line))

    x = np.array(xdata, dtype='float64')
    y = np.array(ydata, dtype='float64')

    curve.setData(x, y, pen=None, symbol='o')

    app.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

## Start the Qt event loop
sys.exit(app.exec_())