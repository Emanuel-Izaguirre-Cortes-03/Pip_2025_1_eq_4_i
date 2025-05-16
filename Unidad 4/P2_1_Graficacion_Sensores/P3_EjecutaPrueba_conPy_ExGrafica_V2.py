import sys
from PyQt5 import uic, QtWidgets, QtGui

import Plantilla_Grafica as interfaz

from matplotlib import pyplot as plt
import random as rnd

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        x = [i for i in range(10)]  # 0, 1, 2 .... 9

        y = []
        for i in x:
            y.append(rnd.randint(0, 1023)) #valores de los sensores

        print(x)
        print(y)

        self.ax.plot(x, y)
        self.canvas.draw()

    #Area de Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

