import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import serial

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

        plotButton = QPushButton('button name', self)
        plotButton.setToolTip('tool tip discription')
        plotButton.move(100, 70)
        plotButton.clicked.connect(self.on_click)

        self.show()
    @pyqtSlot()
    def on_click(self):
        ser = serial.Serial

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())