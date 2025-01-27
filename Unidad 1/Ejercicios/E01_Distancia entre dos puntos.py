import sys
import math
from PyQt5 import QtWidgets, uic


class DistanciaApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui (debe estar en el mismo directorio)
        uic.loadUi("E01_Distancia entre dos puntos.ui", self)

        # Conectar el botón al método para calcular la distancia
        self.btn_calcular.clicked.connect(self.calcular_distancia)

    def calcular_distancia(self):
        try:
            # Obtener valores de los campos de entrada
            x1 = float(self.x1LineEdit.text())
            y1 = float(self.y1LineEdit.text())
            x2 = float(self.x2LineEdit.text())
            y2 = float(self.y2LineEdit.text())

            # Calcular la distancia entre los puntos
            distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Mostrar el resultado
            self.resultadoLabel.setText(f"Distancia: {distancia:.2f}")
        except:
            # Mostrar un mensaje de error simple
            self.resultadoLabel.setText("Error: ingresa números válidos.")


# Iniciar la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = DistanciaApp()
    ventana.show()
    sys.exit(app.exec_())
