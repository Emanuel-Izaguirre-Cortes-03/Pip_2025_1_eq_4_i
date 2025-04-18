import sys
import serial as placa
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P42_ArduinoPythonGUI_ReadWrite_VariosActuadores_v2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.btn_led0.clicked.connect(self.control)
        self.btn_led1.clicked.connect(self.control)
        self.btn_led2.clicked.connect(self.control)

        self.led_estado = [False, False, False]  # Estado de LEDs como lista

    def control(self):
        objeto = self.sender()
        if self.arduino and self.arduino.isOpen():
            led = int(objeto.objectName()[-1])  # Obtener el número del LED
            texto = objeto.text()

            if texto == "PRENDER":
                objeto.setText("APAGAR")
                self.led_estado[led] = True
                c = f"{led}1"
            else:
                objeto.setText("PRENDER")
                self.led_estado[led] = False
                c = f"{led}0"

            self.arduino.write(c.encode())

    def lecturas(self):
        if self.arduino and self.arduino.isOpen():
            try:
                if self.arduino.inWaiting():
                    lectura = self.arduino.readline().decode().strip()
                    if lectura:
                        print(lectura)
                        lectura = lectura.split("@")[:-1]

                        if len(lectura) == 3:
                            sensores = [int(i) for i in lectura]
                            listas_datos = [self.lista_datos0, self.lista_datos1, self.lista_datos2]

                            for i in range(3):
                                if self.led_estado[i]:
                                    listas_datos[i].addItem(str(sensores[i]))
                                    listas_datos[i].setCurrentRow(listas_datos[i].count() - 1)
            except Exception as e:
                print(f"Error en la lectura serial: {e}")

    def accion(self):
        texto = self.btn_accion.text().upper()
        try:
            if texto == "CONECTAR":
                com = "COM" + self.txt_com.text()
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
                self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
            elif texto == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.txt_estado.setText("DESCONECTADO")
                self.segundoPlano.stop()
                self.arduino.close()
            else:
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
                self.arduino.open()
                self.segundoPlano.start(100)
        except Exception as e:
            print(f"Error en la conexión serial: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
