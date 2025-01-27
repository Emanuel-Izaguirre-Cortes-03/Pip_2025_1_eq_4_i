from PyQt5 import QtWidgets, uic


class AreaCuadradoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(AreaCuadradoApp, self).__init__()
        # Cargar la interfaz desde el archivo .ui
        uic.loadUi("E03_Área de un cuadrado.ui", self)

        # Conectar widgets
        self.inputLado = self.findChild(QtWidgets.QLineEdit, "inputLado")
        self.btnCalcular = self.findChild(QtWidgets.QPushButton, "btnCalcular")
        self.lblResultado = self.findChild(QtWidgets.QLabel, "lblResultado")

        # Conectar el botón a la función calcular_area
        self.btnCalcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        try:
            lado = float(self.inputLado.text())
            if lado < 0:
                self.lblResultado.setText("El lado debe ser positivo.")
            else:
                area = lado ** 2
                self.lblResultado.setText(f"Área: {area:.2f} cm² ")
        except ValueError:
            self.lblResultado.setText("Por favor, introduce un número válido.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = AreaCuadradoApp()
    window.show()
    sys.exit(app.exec_())
