import sys
import Recursos_rc
from PyQt5 import uic, QtWidgets, QtGui,QtCore
qtCreatorFile = "P09_SegundoPlano.ui"  # Nombre del archivo aquí.
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
            self.value = int (self.txt_temporizador.text() )
            self.segundoPlano.start(250)

    def temporizadorV2(self):
            if self.value>0:
                self.value -= 1
                self.txt_temporizador.setText(str(self.value))
            else:
                self.segundoPlano.stop()


    #def temporizador(self):
     #       import time as t
      #      valor = int (self.txt_temporizador.text())
       #     for v in range(valor,0,-1):
        #        self.txt_temporizador.setText(str(v))
         #       t.sleep(0.25)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())