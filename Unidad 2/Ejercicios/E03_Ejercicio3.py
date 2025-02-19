import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc
qtCreatorFile = "E03_Ejercicio3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_salir.clicked.connect(self.salir)

    # Área de los Slots
    def calcular(self):
        try:
            num=float(self.txt_ml.text())
            #Conversion
            lt=(num/1000)
            self.txt_lt.setText("{:.5f}".format(lt))
        except ValueError:
            self.msj("Error... Ingresa un valor numerico.")

    def reiniciar(self):
        self.txt_ml.clear()
        self.txt_lt.clear()

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