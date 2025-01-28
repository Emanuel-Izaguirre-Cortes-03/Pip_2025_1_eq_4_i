import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E06_imprimir en consolaMessageBox una tabla de multiplicar.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_sumar.clicked.connect(self.suma)

    # Área de los Slots
    def suma(self):
        try:
            num1 = int(self.txt_A.text())  
            resultado = f"Tabla de multiplicar del {num1}\n"

            for i in range(1, 11):
                resultado += f"{num1} x {i} = {num1 * i}\n"

            self.msj(resultado)
        except ValueError:
            self.msj("Por favor, ingrese un número válido.")
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

