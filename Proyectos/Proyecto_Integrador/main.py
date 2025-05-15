import sys
import serial
import serial.tools.list_ports
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import recursos2_rc  # ← esta línea es importante

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)
        self.setStyleSheet("QMainWindow { border: 2px solid black; }")

        self.arduino = None  # objeto de conexión serie

        # Conexiones de botones
        self.btnConectar.clicked.connect(self.conectar_arduino)
        self.btnDesconectar.clicked.connect(self.desconectar_arduino)
        self.comboServicios.currentIndexChanged.connect(self.cambiar_pagina)
        self.btnEncenderLuz.clicked.connect(self.encender_luz)
        self.btnApagarLuz.clicked.connect(self.apagar_luz)
        self.btnAutomatico.clicked.connect(self.modo_automatico)


        # Conexiones para el Detector de Movimiento
        self.btnActivarSensor.clicked.connect(self.activar_sensor_movimiento)
        self.btnDesactivarSensor.clicked.connect(self.desactivar_sensor_movimiento)

    def modo_automatico(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'AUTO\n')
            QMessageBox.information(self, "Modo Automático", "Modo automático activado.")
            print("[✓] Modo automático activado.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay conexión con Arduino")

    def cambiar_pagina(self, index):
        self.stackServicios.setCurrentIndex(index)
        if self.arduino and self.arduino.is_open:
            if index == 0:
                self.arduino.write(b'SERV1\n')  # Servicio de luz automática
                print("[✓] Activado servicio 1 (Luz automática)")
            elif index == 1:
                self.arduino.write(b'SERV2\n')  # Servicio de movimiento
                print("[✓] Activado servicio 2 (Detector de movimiento)")
        else:
            print("[!] No se envió comando, Arduino no conectado.")

    def conectar_arduino(self):
        puerto_usuario = self.inputCOM.text().strip()

        if not puerto_usuario.upper().startswith("COM"):
            puerto = f"COM{puerto_usuario}"
        else:
            puerto = puerto_usuario

        try:
            self.arduino = serial.Serial(puerto, 9600, timeout=1)
            QMessageBox.information(self, "Conexión Exitosa", f"Conectado a {puerto}")
            print(f"[✓] Conectado al Arduino por {puerto}")
        except serial.SerialException:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al puerto {puerto}")
            print(f"[X] Error al conectar al puerto {puerto}")

    def desconectar_arduino(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            QMessageBox.information(self, "Desconectado", "El Arduino fue desconectado correctamente.")
            print("[✓] Arduino desconectado.")
            self.arduino = None
        else:
            QMessageBox.warning(self, "Advertencia", "No hay conexión activa.")
            print("[!] No hay conexión que cerrar.")

    def encender_luz(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'ON\n')
            print("Luz encendida")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay conexión con Arduino")

    def apagar_luz(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'OFF\n')
            print("Luz apagada")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay conexión con Arduino")

    def activar_sensor_movimiento(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'M')  # Comando para activar sensor
            self.lblEstadoMovimiento.setText("Sensor Activado - Esperando detección…")
            print("[✓] Sensor PIR activado.")
        else:
            QMessageBox.warning(self, "Error", "Primero conecta el Arduino.")

    def desactivar_sensor_movimiento(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'N')  # Comando para desactivar sensor
            self.lblEstadoMovimiento.setText("Sensor Desactivado")
            print("[✓] Sensor PIR desactivado.")
        else:
            QMessageBox.warning(self, "Error", "Primero conecta el Arduino.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
