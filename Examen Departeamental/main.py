import sys
import serial
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QStringListModel
from PyQt5.QtGui import QPixmap
import Archivos.recursos_rc  # Importa el archivo generado
import re

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)  # Carga tu archivo .ui
        self.arduino = None
        self.timer = QTimer(self)  # Temporizador para leer datos del Arduino
        self.timer.timeout.connect(self.leer_datos_arduino)

        # Modelo para el QListView
        self.datos_sensor = []
        self.modelo_lista = QStringListModel(self.datos_sensor)
        # self.listView.setModel(self.modelo_lista) # Comentado porque se usará QListWidget

        # Conectar botones a sus funciones
        self.btnConectar.clicked.connect(self.conectar_arduino)
        self.btnDesconectar.clicked.connect(self.desconectar_arduino)
        self.btnEncenderLuz.clicked.connect(self.encender_luz)
        self.btnApagarLuz.clicked.connect(self.apagar_luz)

    def conectar_arduino(self):
        puerto = self.inputCOM.text().strip()
        if not puerto:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa un puerto COM válido.")
            return

        try:
            self.arduino = serial.Serial(f"COM{puerto}", 9600, timeout=1)
            QMessageBox.information(self, "Conexión", f"Arduino conectado correctamente en COM{puerto}.")
            self.timer.start(100)  # Leer datos cada 100 ms
        except serial.SerialException as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar al Arduino en COM{puerto}. Verifica el puerto.\n{e}")
        except ValueError:
            QMessageBox.critical(self, "Error", "El puerto COM ingresado no es válido.")

    def desconectar_arduino(self):
        if self.arduino:
            self.arduino.close()
            self.arduino = None
            QMessageBox.information(self, "Desconexión", "Arduino desconectado correctamente.")
            self.timer.stop()
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ninguna conexión activa.")

    def encender_luz(self):
        if self.arduino:
            self.arduino.write(b'1')  # Activar servicio 1
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def apagar_luz(self):
        if self.arduino:
            self.arduino.write(b'0')  # Desactivar servicio 1
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def leer_datos_arduino(self):
        if self.arduino and self.arduino.in_waiting > 0:
            try:
                linea = self.arduino.readline().decode('utf-8', errors='ignore').strip()
                match = re.match(r"(\d+)", linea)
                if match:
                    valor = int(match.group(1))
                    porcentaje = int((valor / 1023) * 100)  # Si tu LDR va de 0 a 1023
                    barra = "▇" * (porcentaje // 5)  # 20 bloques máximo
                    texto = f"Luz: {valor}  [{barra:<20}] {porcentaje}%"
                    self.datos_sensor.append(texto)
                    self.datos_sensor = self.datos_sensor[-20:]
                    self.listWidget.clear()
                    self.listWidget.addItems(self.datos_sensor)
            except Exception as e:
                pass  # Ya no imprime errores en la terminal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
