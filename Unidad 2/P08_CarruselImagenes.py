import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_CarruselImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.valueChanged.connect(self.cambiaValor)
        self.selectorImagen.setMinimum(0)
        self.selectorImagen.setMaximum(2)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(0)

        #label_2
        self.datosImagenes={
        0: [":/Archivos/UAT.png", "UAT"],
        1: [":/Archivos/Castor.jpg", "Castor"],
        2: [":/Archivos/facultad_ingenieria_tampico.png", "La facultad de ingenieria"],
        }
        self.cambiaValor()

    # Área de los Slots
    def cambiaValor(self):
        valor=self.selectorImagen.value()

        imagen_ruta = self.datosImagenes[valor][0]
        self.imagen_nombre.setPixmap(QtGui.QPixmap())

        imagen_nombre = self.datosImagenes[valor][1]
        self.txt_nombre_imagen.setText(imagen_nombre)

        print(f"Imagen: {imagen_nombre}, Índice: {valor}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())