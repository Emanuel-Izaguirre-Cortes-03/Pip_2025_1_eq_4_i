import random
import sys
from PyQt5 import uic, QtWidgets, QtGui
import Recursos_rc  # Asegúrate de que existe y compila bien

qtCreatorFile = "PP1.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configuración del QSlider
        self.selectorImagen.valueChanged.connect(self.cambiaValor)
        self.selectorImagen.setMinimum(0)
        self.selectorImagen.setMaximum(2)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(0)

        # Botón para verificar
        self.btn_aceptar.clicked.connect(self.Verificar)

        # Diccionario con rutas e identificadores
        self.datosImagenes = {
            0: [":/Logos/UAT.png", "UAT"],
            1: [":/Logos/Castor.jpg", "Castor programador"],
            2: [":/Logos/facultad_ingenieria_tampico.png", "La facultad de ingeniería..."],
        }

        self.cambiaValor()
        self.seleccionAleatoria()

    def cambiaValor(self):
        """Actualiza la imagen según la posición del slider."""
        valor = self.selectorImagen.value()
        self.ruta_imagen = self.datosImagenes[valor][0]

        pixmap = QtGui.QPixmap(self.ruta_imagen)
        if not pixmap.isNull():
            self.label_2.setPixmap(QtGui.QPixmap(r"C:\Users\Emanu\Documents\Pip_2025_1_eq_4_i\Logos\UAT.png"))

            self.label_2.setScaledContents(True)  # Ajusta la imagen al QLabel
        else:
            print(f"Error: No se pudo cargar la imagen {self.ruta_imagen}")

    def Verificar(self):
        """Verifica si el texto ingresado coincide con la descripción de la imagen."""
        try:
            texto = self.txt_nombre_imagen.text()
            if self.datosImagenes[self.selectorImagen.value()][1] == texto:
                self.msj("Bien", "Es correcto")
                self.seleccionAleatoria()
            else:
                self.msj("Mal", "Es incorrecto")
        except Exception as e:
            print(e)

    def seleccionAleatoria(self):
        """Selecciona aleatoriamente una imagen y actualiza el slider y el texto."""
        n = random.choice(list(self.datosImagenes.keys()))
        texto = self.datosImagenes[n][1]
        self.txt_nombre_imagen.setText(texto)
        self.selectorImagen.setValue(n)

    def msj(self, title, txt):
        """Muestra un QMessageBox informativo."""
        m = QtWidgets.QMessageBox()
        m.setIcon(QtWidgets.QMessageBox.Information)
        m.setWindowTitle(title)
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
