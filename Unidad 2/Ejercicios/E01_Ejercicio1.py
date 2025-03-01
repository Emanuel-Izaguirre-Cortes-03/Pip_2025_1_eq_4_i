import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc

qtCreatorFile = "E01_Ejercicio1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_salir.clicked.connect(self.salir)

    # Área de los Slots
    def calcular(self):
        try:
            num = float(self.txt_centigrados.text())
            # Conversión
            f = (num * 9 / 5) + 32
            self.txt_farenheit.setText("{:.2f}".format(f))  # Asegura que sea el nombre correcto del objeto
        except ValueError:
            self.msj("Error... Ingresa un valor numérico.")

    def reiniciar(self):
        self.txt_centigrados.clear()
        self.txt_farenheit.clear()

    def salir(self):
        self.close()

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
