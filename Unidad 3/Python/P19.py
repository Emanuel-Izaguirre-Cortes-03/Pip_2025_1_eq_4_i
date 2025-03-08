import serial as  control
from matplotlib import pyplot as plt

arduino =control.Serial("COM4",baudrate=9600,timeout=1)
while True:
   v= input("valor de control para el led:")
   arduino.write(v.encode())



