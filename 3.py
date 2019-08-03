import serial
from tkinter import *
import tkinter
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

COM = "COM14" #COM port
BAUD = 9600   #Baudrate
ser = serial.Serial(COM, BAUD)

while 1:
    ser.write(b'w')

    // mode = Serial.read();
    // while (mode != '1' | | mode != 3){
    // switch(mode){// move acording to input
    // case 'w': forward();
    //
    case
    'a': left();
    // case
    's': reverse();
    // case
    'd': right();
    // case
    ' ': stop_m();
    // case
    'S': scan();
    // case
    'D': deliver();
    // default: stop_m();
    //}
    // mode = Serial.read();
    //}