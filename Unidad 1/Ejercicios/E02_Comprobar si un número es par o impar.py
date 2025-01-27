from PyQt5 import QtWidgets, uic


class ParImparApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ParImparApp, self).__init__()
        # Carga la interfaz .ui
        uic.loadUi("E02_Comprobar si un número es par o impar.ui", self)

        # Conectar elementos
        self.inputNumber = self.findChild(QtWidgets.QLineEdit, "inputNumber")
        self.btnCheck = self.findChild(QtWidgets.QPushButton, "btnCheck")
        self.lblResult = self.findChild(QtWidgets.QLabel, "lblResult")

        # Conectar botón al método
        self.btnCheck.clicked.connect(self.check_par_impar)

    def check_par_impar(self):
        try:
            numero = int(self.inputNumber.text())
            if numero % 2 == 0:
                self.lblResult.setText("Es par")
            else:
                self.lblResult.setText("Es impar")
        except ValueError:
            self.lblResult.setText("Por favor, introduce un número válido")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ParImparApp()
    window.show()
    sys.exit(app.exec_())
