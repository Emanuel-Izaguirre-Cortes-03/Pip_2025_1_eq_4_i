import sys
import Recursos_rc
from PyQt5 import QtWidgets, QtCore
from PP2_ui import Ui_MainWindow  # Importamos la interfaz corregida

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inicialización del temporizador y variable de tiempo
        self.tiempo_transcurrido = 0
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizadorV2)

        # Conectar botón a la función para iniciar el temporizador
        self.btn_temporizador.clicked.connect(self.iniciarTempo)

    def iniciarTempo(self):
        """Inicia el temporizador y reinicia el contador."""
        self.tiempo_transcurrido = 0  # Reinicia el contador de tiempo
        self.segundoPlano.start(1000)  # Configura el temporizador para que se ejecute cada 1 segundo

    def temporizadorV2(self):
        """Actualiza el temporizador cada segundo."""
        self.tiempo_transcurrido += 1
        self.label_tiempo.setText(f"Tiempo: {self.tiempo_transcurrido} s")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
