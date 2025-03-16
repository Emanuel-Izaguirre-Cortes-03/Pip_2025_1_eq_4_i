import sys
import random
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi


class SimonDice(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("simon_dice.ui", self)

        # Cargar imágenes de los logos
        self.cargar_logos()

        self.secuencia = []
        self.indice_usuario = 0
        self.puntaje = 0
        self.juego_activo = False  # Para evitar errores al reiniciar

        self.colores = {"rojo": self.btn_rojo, "azul": self.btn_azul,
                        "verde": self.btn_verde, "amarillo": self.btn_amarillo}

        for color, boton in self.colores.items():
            boton.clicked.connect(lambda _, c=color: self.boton_presionado(c))
        self.btn_inicio.clicked.connect(self.iniciar_juego)

    def cargar_logos(self):
        """Carga los logos en los QLabel de la interfaz."""
        if hasattr(self, "lbl_logo_izquierdo") and hasattr(self, "lbl_logo_derecho"):
            # Verifica si existen las etiquetas en el .ui
            ruta_logo_izq = os.path.abspath("logo_izquierdo.png")
            ruta_logo_der = os.path.abspath("logo_derecho.png")

            if os.path.exists(ruta_logo_izq):
                self.lbl_logo_izquierdo.setPixmap(QPixmap(ruta_logo_izq))
                self.lbl_logo_izquierdo.setScaledContents(True)

            if os.path.exists(ruta_logo_der):
                self.lbl_logo_derecho.setPixmap(QPixmap(ruta_logo_der))
                self.lbl_logo_derecho.setScaledContents(True)

    def iniciar_juego(self):
        self.secuencia.clear()
        self.puntaje = 0
        self.indice_usuario = 0
        self.juego_activo = True  # Activar juego
        self.actualizar_puntaje()
        self.nueva_ronda()

    def nueva_ronda(self):
        if not self.juego_activo:
            return  # Evitar que la secuencia siga ejecutándose tras reiniciar
        self.indice_usuario = 0
        self.secuencia.append(random.choice(list(self.colores.keys())))
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        for i, color in enumerate(self.secuencia):
            QTimer.singleShot(i * 1000, lambda c=color: self.iluminar_boton(c))

    def iluminar_boton(self, color):
        boton = self.colores[color]
        boton.setStyleSheet("background-color: white;")
        QTimer.singleShot(500, lambda: boton.setStyleSheet(""))

    def boton_presionado(self, color):
        if not self.juego_activo:
            return  # Evitar interacciones si el juego ha sido reiniciado

        if color == self.secuencia[self.indice_usuario]:
            self.indice_usuario += 1
            if self.indice_usuario == len(self.secuencia):
                self.puntaje += 1
                self.actualizar_puntaje()
                QTimer.singleShot(1000, self.nueva_ronda)
        else:
            self.juego_activo = False  # Evitar errores con secuencias antiguas
            QMessageBox.warning(self, "Fin del juego", "Te equivocaste. Inténtalo de nuevo.")
            self.iniciar_juego()

    def actualizar_puntaje(self):
        self.lbl_puntaje.setText(f"Puntaje: {self.puntaje}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SimonDice()
    ventana.show()
    sys.exit(app.exec_())
