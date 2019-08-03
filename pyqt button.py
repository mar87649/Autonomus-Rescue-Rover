import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import serial
COM = "COM11"
BAUD = 9600

ser = serial.Serial(COM, BAUD)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'window title'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        Button = QPushButton('button name', self)
        Button.setToolTip('tool tip discription')
        Button.move(100, 70)
        Button.clicked.connect(self.on_click)

        self.show()
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        ser.write(b' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())