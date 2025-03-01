import sys
import recursos_rc
from PyQt5 import uic, QtWidgets, QtGui,QtCore
qtCreatorFile = "PP2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_temporizador.clicked.connect(self.iniciarTempo)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizadorV2)

    def iniciarTempo(self):
       pass

    def temporizadorV2(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())