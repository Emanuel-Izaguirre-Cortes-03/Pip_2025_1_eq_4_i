import math
import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc
qtCreatorFile = "E08_Ejercicio8.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_salir.clicked.connect(self.salir)

    # Área de los Slots
    def aceptar(self):
        try:
            numero1 = self.txt_numero.text().strip()
            numero = int(numero1)
            tabla = ""
            if numero >= 0:
                for i in range(1, 11):
                    tabla += f"{numero}x{i}={numero * i}\n"
                self.msj("Resultado", f"Tabla de multiplicar del {numero}:\n\n{tabla}")

                # imprime en consola
                print("Resultado", f"Tabla de multiplicar del {numero}:\n\n{tabla}")
                self.txt_numero.clear()
            else:
                self.msj("Resultado", "Ingresa un numero positivo")
        except ValueError:
            self.msj("Error", "Ingresa un numero valido")

    def salir(self):
        self.close()

    def msj(self, title, txt):
        m = QtWidgets.QMessageBox()
        m.setIcon(QtWidgets.QMessageBox.Information)
        m.setWindowTitle(title)
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())