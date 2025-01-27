import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ventana.ui', self)
        self.boton_calcular.clicked.connect(self.calcular_horas_restantes)

    def calcular_horas_restantes(self):
        try:
            hora = int(self.entrada_hora.text())
            if 0 <= hora < 24:
                horas_restantes = 24 - hora
                self.resultado.setText(f"Quedan {horas_restantes} horas para que termine el día.")
            else:
                self.resultado.setText("Por favor, ingresa una hora válida (0-23).")
        except ValueError:
            self.resultado.setText("Por favor, ingresa un número válido.")

app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec_())

# Pausa al final del programa
input("Presiona Enter para salir...")