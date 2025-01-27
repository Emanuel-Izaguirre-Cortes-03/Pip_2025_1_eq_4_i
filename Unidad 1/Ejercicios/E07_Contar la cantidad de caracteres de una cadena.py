import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ventana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ventana2.ui', self)
        self.boton_contar.clicked.connect(self.contar_caracteres)

    def contar_caracteres(self):
        cadena = self.entrada_cadena.text()
        cantidad_caracteres = len(cadena)
        self.resultado.setText(f"La cantidad de caracteres es: {cantidad_caracteres}")

app = QApplication(sys.argv)
ventana = Ventana2()
ventana.show()
sys.exit(app.exec_())