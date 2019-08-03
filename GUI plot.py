import sys
import numpy as np
import pyqtgraph as pg
import serial
from pyqtgraph.Qt import QtGui, QtCore

#set up serial communication
ser = serial.Serial("COM11", 9600)

# Set white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

# # Generate random points
# n = 1000
# print('Number of points: ' + str(n))
# data = np.random.normal(size=(2, n))

#Generate Data
datax = 0
datay = ser.readline()

# Create the main application instance
#app = pg.mkQApp()
app = QtGui.QApplication([])

# Create the view
view = pg.PlotWidget()
view.resize(800, 600)
view.setWindowTitle('Scatter plot using pyqtgraph with PyQT5')
view.setAspectLocked(True)
view.show()

# Create the scatter plot and add it to the view
scatter = pg.ScatterPlotItem(pen=pg.mkPen(width=5, color='r'), symbol='o', size=1)
view.addItem(scatter)

# Convert data array into a list of dictionaries with the x,y-coordinates
def update():
    data = 0
    line = ser.readline()
    data.append(int(line))
    xdata = 0
    ydata = np.array(data, dtype='float64')

    scatter.setData(xdata, ydata)

# Gracefully exit the application
sys.exit(app.exec_())

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()