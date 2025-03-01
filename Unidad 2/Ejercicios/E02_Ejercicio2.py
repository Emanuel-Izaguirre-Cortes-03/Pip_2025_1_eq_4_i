import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E02_ConversorHoras.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Conexión de botones a funciones
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_salir.clicked.connect(self.salir)

    def calcular(self):
        try:
            # Obtener la hora ingresada
            tiempo = self.txt_hora.text()  # Formato esperado HH:MM:SS
            partes = tiempo.split(":")

            if len(partes) != 3:
                raise ValueError  # Si el formato es incorrecto

            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])

            # Validaciones básicas
            if not (0 <= horas < 24 and 0 <= minutos < 60 and 0 <= segundos < 60):
                raise ValueError

            # Convertir a segundos
            total_segundos = (horas * 3600) + (minutos * 60) + segundos

            # Mostrar resultado
            self.txt_segundos.setText(str(total_segundos))

        except ValueError:
            self.msj("Error... Ingresa una hora válida en formato HH:MM:SS")

    def reiniciar(self):
        self.txt_hora.clear()
        self.txt_segundos.clear()

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
