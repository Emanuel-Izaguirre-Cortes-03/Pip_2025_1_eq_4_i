import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_DescripcionDeImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(1)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1) ##valr inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            0: (":/Ejercicios/ImagenGatoEuropeo.png",["Gato", "4 meses", "Raton"]),
            1: (":/Logos/FIT_logo_vertical.png", ["Castor", "65 años", "Estudiar"]),
            2: (":/Logos/log_uat_nuevo.png", ["Correcaminos", "75 años", "Superacion"])
        }
        self.indice = 0
        self.obtenerDatos()

    # Área de los Slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        juguete = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_juguete.setText(juguete)

    def cambiaValor(self):
        value = self.selectorImagen.value()
        #self.txt_valor.selectorImagen(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

