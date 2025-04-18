import sys
import serial as placa
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P41_ArduinoPythonGUI_ReadWrite_VariosActuadores.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.btn_led0.clicked.connect(self.control)
        self.btn_led1.clicked.connect(self.control)
        self.btn_led2.clicked.connect(self.control)

        #Area de los Slots

    def control(self):
        objeto = self.sender()
        if self.arduino.isOpen():
            led = objeto.objectName()[-1]
            texto = objeto.text()
            if texto == "PRENDER":
                objeto.setText("APAGAR")
                c = led + "1"
                self.arduino.write(c.encode())
            else:
                objeto.setText("PRENDER")
                c = led + "0"
                self.arduino.write(c.encode())

    def lecturas(self):
        if self.arduino.isOpen(): #La comunicacion esta abierta.....
            if self.arduino.inWaiting(): #Hay informacion que leer....
                lectura = self.arduino.readline().decode().strip()
                if lectura !="":
                    print(lectura)
                    #PROCESAMIENTO DE LOS DATOS...
                    lectura = lectura.split("@")
                    lectura = lectura[:-1]

                    lectura = [int(i) for i in lectura]

                    self.lista_datos.addItem(str(lectura))
                    self.lista_datos.setCurrentRow(self.lista_datos.count()-1)

    def accion(self):
        texto = self.btn_accion.text().upper()
        if texto == "CONECTAR": #Inicia la comunicacion y la apertura
            com = "COM" + self.txt_com.text()
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
        elif texto == "DESCONECTAR": #Cierra la comunicacion
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            self.segundoPlano.stop()
            self.arduino.close()
        else: #Reapertura la comunicacion
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            self.arduino.open()
            self.segundoPlano.start(100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
