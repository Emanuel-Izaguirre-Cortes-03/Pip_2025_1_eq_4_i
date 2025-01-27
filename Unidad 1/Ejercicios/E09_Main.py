import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from factorial import Ui_MainWindow


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar el botón con la función que calcula el factorial
        self.pushButton.clicked.connect(self.calcular_factorial)

    def calcular_factorial(self):
        numero = int(self.lineEdit.text())
        resultado = factorial(numero)
        self.label.setText(f"El factorial de {numero} es {resultado}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
