import sys
import serial
import csv
import os
import pandas as pd
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
import Archivos.recursos_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)
        self.arduino = None
        self.datos_ldr = []
        self.datos_pir = []
        self.datos_temp = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.leer_dato_ldr)
        self.timer_pir = QTimer(self)
        self.timer_pir.timeout.connect(self.leer_dato_pir)
        self.timer_temp = QTimer(self)
        self.timer_temp.timeout.connect(self.leer_dato_temp)

        # Conexión de botones
        self.btnConectar.clicked.connect(self.conectar_arduino)
        self.btnDesconectar.clicked.connect(self.desconectar_arduino)
        self.btnEncenderLuz.clicked.connect(self.encender_luz)
        self.btnApagarLuz.clicked.connect(self.apagar_luz)
        self.btnGraficarLuz.clicked.connect(self.graficar_ldr)
        self.btnExportarDatos.clicked.connect(self.exportar_ldr)
        self.btnEncenderMovimiento.clicked.connect(self.encender_movimiento)
        self.btnApagarMovimiento.clicked.connect(self.apagar_movimiento)
        self.btnGraficarPIR.clicked.connect(self.graficar_pir)
        self.btnExportarPIR.clicked.connect(self.exportar_pir)
        self.btnEncenderTemp.clicked.connect(self.encender_temp)
        self.btnApagarTemp.clicked.connect(self.apagar_temp)
        self.btnGraficarTemp.clicked.connect(self.graficar_temp)
        self.btnExportarTemp.clicked.connect(self.exportar_temp)
        self.comboBoxServicio.currentIndexChanged.connect(self.cambiar_servicio)

    def conectar_arduino(self):
        puerto = self.inputCOM.text().strip()
        if not puerto:
            QMessageBox.warning(self, "Advertencia", "Ingresa un puerto COM válido.")
            return
        try:
            self.arduino = serial.Serial(f"COM{puerto}", 9600, timeout=1)
            QMessageBox.information(self, "Conexión", f"Arduino conectado en COM{puerto}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar: {e}")

    def desconectar_arduino(self):
        if self.arduino:
            self.arduino.close()
            self.arduino = None
            QMessageBox.information(self, "Desconexión", "Arduino desconectado.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay conexión activa.")

    def encender_luz(self):
        if self.arduino:
            self.arduino.write(b'L1\n')
            print("Enviado: L1")  # <-- depuración
            self.lblEstado.setText("Luz encendida")
            self.timer.start(200)  # Inicia la lectura periódica
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def apagar_luz(self):
        if self.arduino:
            try:
                self.arduino.write(b'L0\n')  # Apaga el servicio en Arduino
                print("Enviado: L0")         # Depuración
            except Exception as e:
                print(f"Error enviando L0: {e}")
            self.lblEstado.setText("Luz apagada")
            self.timer.stop()                # Detiene la lectura periódica
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def leer_dato_ldr(self):
        if self.arduino and self.arduino.in_waiting > 0:
            try:
                dato = self.arduino.readline().decode().strip()
                if dato.startswith("LDR:"):
                    valor = dato.split(":")[1].strip()
                    porcentaje = int(int(valor) / 1023 * 100)
                    bloques = int(porcentaje / 5)
                    barra = "█" * bloques + " " * (20 - bloques)
                    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    texto = f"[{fecha_hora}] Luz: {valor}  |{barra}| {porcentaje}%"
                    # Guarda los datos como tuplas para exportar igual que el ListWidget
                    self.datos_ldr.append((fecha_hora, valor, barra, porcentaje))
                    self.listViewLDR.addItem(texto)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo leer dato: {e}")

    def leer_dato_pir(self):
        if self.arduino and self.arduino.in_waiting > 0:
            try:
                dato = self.arduino.readline().decode().strip()
                if dato.startswith("DIST:"):
                    distancia = dato.split(":")[1].strip()
                    pir_line = self.arduino.readline().decode().strip()
                    if pir_line.startswith("PIR:"):
                        movimiento = pir_line.split(":")[1].strip()
                        if movimiento == "1" and float(distancia) <= 50:
                            fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                            texto = f"[{fecha_hora}] Servicio: ACTIVADO | Distancia: {distancia} cm | Movimiento: Sí"
                            self.datos_pir.append((fecha_hora, distancia, "Sí", "ACTIVADO"))
                            self.listViewPIR.addItem(texto)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo leer dato PIR: {e}")

    def leer_dato_temp(self):
        if self.arduino and self.arduino.in_waiting > 0:
            try:
                dato = self.arduino.readline().decode().strip()
                print("Dato recibido:", dato)  # <-- Agrega esta línea
                if dato.startswith("TEMP:"):
                    partes = dato.replace("TEMP:", "").split(",HUM:")
                    temp = partes[0].strip()
                    hum = partes[1].strip()
                    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    texto = f"[{fecha_hora}] Temp: {temp}°C | Humedad: {hum}%"
                    self.datos_temp.append((fecha_hora, temp, hum))
                    self.listViewTemp.addItem(texto)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo leer dato TEMP: {e}")

    def graficar_ldr(self):
        if not self.datos_ldr:
            QMessageBox.warning(self, "Advertencia", "No hay datos para graficar.")
            return

        carpeta = "detector_de_luz_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_grafica = os.path.join(carpeta, f"grafica_LDR_{fecha_archivo}.jpg")
        ruta = os.path.join(carpeta, f"datos_LDR_{fecha_archivo}.xlsx")
        try:
            valores = [float(x[1]) for x in self.datos_ldr]
            plt.figure("Datos LDR")
            plt.plot(valores, marker='o')
            plt.title("Valores del sensor LDR")
            plt.xlabel("Muestra")
            plt.ylabel("Valor LDR")
            plt.grid(True)
            plt.savefig(ruta_grafica)
            plt.close()
            QMessageBox.information(self, "Gráfica", f"Gráfica guardada como:\n{ruta_grafica}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo graficar: {e}")

    def exportar_ldr(self):
        if not self.datos_ldr:
            QMessageBox.warning(self, "Advertencia", "No hay datos para exportar.")
            return

        carpeta = "detector_de_luz_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(carpeta, f"datos_LDR_{fecha_archivo}.xlsx")
        try:
            df = pd.DataFrame(self.datos_ldr, columns=["Fecha/Hora", "Valor LDR", "Barra", "Porcentaje"])
            df.to_excel(ruta, index=False)
            QMessageBox.information(self, "Exportar", f"Datos exportados correctamente en:\n{ruta}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo exportar: {e}")

    def encender_movimiento(self):
        if self.arduino:
            self.arduino.write(b'S2ON\n')
            self.lblEstadoMovimiento.setText("Movimiento activado")
            self.timer_pir.start(100)
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def apagar_movimiento(self):
        if self.arduino:
            self.arduino.write(b'S2OFF\n')
            self.lblEstadoMovimiento.setText("Movimiento apagado")
            self.timer_pir.stop()
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def graficar_pir(self):
        if not self.datos_pir:
            QMessageBox.warning(self, "Advertencia", "No hay datos para graficar.")
            return
        carpeta = "detector_de_movimiento_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_grafica = os.path.join(carpeta, f"grafica_PIR_{fecha_archivo}.jpg")
        ruta = os.path.join(carpeta, f"datos_PIR_{fecha_archivo}.xlsx")
        try:
            distancias = [float(x[1]) for x in self.datos_pir]
            plt.figure("Datos PIR")
            plt.plot(distancias, marker='o')
            plt.title("Distancia detectada por HC-SR04")
            plt.xlabel("Muestra")
            plt.ylabel("Distancia (cm)")
            plt.grid(True)
            plt.savefig(ruta_grafica)
            plt.close()
            QMessageBox.information(self, "Gráfica", f"Gráfica guardada como:\n{ruta_grafica}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo graficar: {e}")

    def exportar_pir(self):
        if not self.datos_pir:
            QMessageBox.warning(self, "Advertencia", "No hay datos para exportar.")
            return
        carpeta = "detector_de_movimiento_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(carpeta, f"datos_PIR_{fecha_archivo}.xlsx")
        try:
            df = pd.DataFrame(self.datos_pir, columns=["Fecha/Hora", "Distancia (cm)", "Movimiento", "Servicio"])
            df.to_excel(ruta, index=False)
            QMessageBox.information(self, "Exportar", f"Datos exportados correctamente en:\n{ruta}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo exportar: {e}")
    def encender_temp(self):
        if self.arduino:
            self.arduino.write(b'S3ON\n')
            if hasattr(self, 'lblEstadoTemp'):
                self.lblEstadoTemp.setText("Temperatura activada")
            self.timer_temp.start(100)
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")

    def apagar_temp(self):
        if self.arduino:
            self.arduino.write(b'S3OFF\n')
            if hasattr(self, 'lblEstadoTemp'):
                self.lblEstadoTemp.setText("Temperatura desactivada")
            self.timer_temp.stop()
        else:
            QMessageBox.warning(self, "Advertencia", "Conecta el Arduino primero.")
    def graficar_temp(self):
        if not self.datos_temp:
            QMessageBox.warning(self, "Advertencia", "No hay datos para graficar.")
            return
        carpeta = "detector_temp_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_grafica = os.path.join(carpeta, f"grafica_TEMP_{fecha_archivo}.jpg")
        try:
            temps = [float(x[1]) for x in self.datos_temp]
            plt.figure("Datos Temperatura")
            plt.plot(temps, marker='o')
            plt.title("Temperatura")
            plt.xlabel("Muestra")
            plt.ylabel("Temp (°C)")
            plt.grid(True)
            plt.savefig(ruta_grafica)
            plt.close()
            QMessageBox.information(self, "Gráfica", f"Gráfica guardada como:\n{ruta_grafica}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo graficar: {e}")

    def exportar_temp(self):
        if not self.datos_temp:
            QMessageBox.warning(self, "Advertencia", "No hay datos para exportar.")
            return
        carpeta = "detector_temp_datos"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(carpeta, f"datos_TEMP_{fecha_archivo}.xlsx")
        try:
            df = pd.DataFrame(self.datos_temp, columns=["Fecha/Hora", "Temperatura (°C)", "Humedad (%)"])
            df.to_excel(ruta, index=False)
            QMessageBox.information(self, "Exportar", f"Datos exportados correctamente en:\n{ruta}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo exportar: {e}")

    def mostrar_servicio_luz(self):
        self.stackedWidget.setCurrentIndex(0)

    def mostrar_servicio_movimiento(self):
        self.stackedWidget.setCurrentIndex(1)

    def cambiar_servicio(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def closeEvent(self, event):
        # Apaga todos los servicios antes de cerrar
        if self.arduino:
            try:
                self.arduino.write(b'L0\n')      # Apaga servicio de luz
                self.arduino.write(b'S2OFF\n')   # Apaga servicio de movimiento
                self.arduino.write(b'S3OFF\n')   # Apaga servicio de temperatura
            except Exception:
                pass
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
