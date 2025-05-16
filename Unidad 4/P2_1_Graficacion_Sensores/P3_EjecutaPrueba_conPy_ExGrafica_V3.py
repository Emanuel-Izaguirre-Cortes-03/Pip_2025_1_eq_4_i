import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

import Plantilla_Grafica as interfaz

from matplotlib import pyplot as plt
import random as rnd

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_graficar.clicked.connect(self.graficar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.x = [i for i in range(70)]  # 0, 1, 2 .... 9
        self.y = []


    #Area de Slots
    def lecturas(self):

        self.y.append(rnd.randint(0, 1023))  # valores de los sensores
        while len(self.y) < len(self.x):
            self.y.append(rnd.randint(0, 1023))  # valores de los sensores
        print(self.x)
        print(self.y)
        yaux = self.y[-70:]
        #print(yaux)
        self.ax.plot(self.x, yaux)
        self.canvas.draw()
        #del self.y[0]
        plt.cla()

    def graficar(self):
        self.segundoPlano.start(100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

