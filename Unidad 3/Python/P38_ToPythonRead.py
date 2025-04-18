import sys
from PyQt5 import uic, QtWidgets,QtCore
import serial as placa
qtCreatorFile = "P38_ToPythonRead.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.arduino=None
        self.btn_accion.clicked.connect(self.accion)


        self.segundoPlano=QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

    # Área de los Slots
    def lecturas(self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting():
                lectura=self.arduino.readline().decode().strip()
                print(lectura)
    def accion(self):

            texto= self.btn_accion.text().upper()
            if texto=="CONECTAR":
                com = "COM"+ self.txt_com.text()


                self.btn_accion.setText("DESCONECTAR")
                self.btn_estado.setText("CONECTADO")
                self.arduino = placa.Serial(com,baudrate=9600,timeout=1)
                self.segundoPlano.start(100)
            elif texto == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.btn_estado.setText("DESCONECTADO")
                self.arduino.close()
            else :
                self.btn_accion.setText("DESCONECTAR")
                self.btn_estado.setText("CONECTADO")
                self.arduino.open()
                self.segundoPlano.start(100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

