import serial as  control
from matplotlib import pyplot as plt

arduino =control.Serial("COM4",baudrate=9600,timeout=1)

tot_Lectura=20
Lectura=0
datos=[]

while Lectura < tot_Lectura:
    mensaje= arduino.readline().decode().strip()
    if mensaje != "":
      print(mensaje)
      datos.append(mensaje)
      Lectura  +=1;

datos=[int(i) for i in datos]

print(datos)

X= [i for i in range(len(datos))]
plt.plot(X,datos)
plt.show()