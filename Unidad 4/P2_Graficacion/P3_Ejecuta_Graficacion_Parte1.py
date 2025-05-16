import sys
from PyQt5 import QtWidgets

import Plantilla_Grafica as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_graficar.clicked.connect(self.graficar)
        #self.btn_limpiar.clicked.connect(self.limpiar)

        #VALORES POR DEFECTO:
        self.configuracion = {
            "estilo_linea": ":",
            "color_linea":"black",
            "ancho_linea":1
        }
        self.limite = {
            "x": [1, 10, 10], #min, max, divisiones
            "y": [1, 10, 10]  #min, max, divisiones
        }

        self.btn_grilla.setText("ON")

    # Área de los Slots
    def graficar(self):
        polinomio = self.txt_polinomio.text()  # Ej: 2x^2+3x+4
        polinomio = polinomio.replace("^","**")  # 2x**2+3x+4

        #tabular...  valores de X con base en los cuales pueda obtener los valores de y
        X = [i for i in range(self.limite["x"][0], self.limite["x"][1])] #lista de comprension
        print("Valores de X: ")
        print(X)

        #y = polinomio.replace("x","*("+str(x[0])+")")  #2*(X[0])**2+3*(X[0])+4
        y = [eval(polinomio.replace("x","*("+str(x)+")")) for x in X]
        print("Valores de Y: ")
        print(y)

        self.ax.plot(X, y,
                 linestyle= self.configuracion["estilo_linea"],  #: - -- -.
                 color= self.configuracion["color_linea"],  # color de la linea
                 linewidth= self.configuracion["ancho_linea"],  # tamaño de la linea
                 marker=".",  # o . *  x   1
                 markersize=4,
                 markerfacecolor="yellow",  # color interno del marcador
                 markeredgewidth=1,  # tamaño del borde del marcador
                 markeredgecolor="blue",  # color del borde del marcador
                 dash_capstyle="butt",  # dash or solid : "butt" "round" "projecting"
                 dash_joinstyle="miter"  # dash or solid : "miter" "round" "bevel"
                 )

        self.canvas.draw()

        #Establecer los limites
        #self.ax.set_xlim(self.xMin, self.xMax+1)
        #self.ax.set_ylim(self.yMin, self.yMax + 1)

        #self.ax.set_xlabel("Eje X")
        #self.ax.set_ylabel("Eje Y")

        #totalelementosenX/totaldivisionesDeseadas = 8
        #mediante un ciclo se obtiene:

        #si comienzo con xmin en 0 seria:
        #xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        #si comienzo con xmin en n seria:
        #xtick = []
        #for i in range(-30, 30+1, 10):
        #    xtick.append(i)
        #print("Ticks para X: ")
        #print(xtick)


        #xtick = [2, 5, 15, 25, 35, 45, 55, 65, 75, 85]


        #self.ax.set_xticks(xtick)


        #self.ax.set_yticks(y)   #NOTA.. CHECK!

        #una posibilidad para establecer los ticks sería:
        #Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee


    def limpiar(self):
        plt.cla()    #borra_todo
        self.canvas.draw()  #vuelve a dibujar

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
