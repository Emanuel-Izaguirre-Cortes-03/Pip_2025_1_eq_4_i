'''

generar aleatoriamente en caja texto, nombre de imaegen, abajo imagen y slider , aceptar , si coincide la imagen y el texto correcto

simular funcionamiento reloj 24 establecer hora manualmente
'''
import random
from winreg import error
import sys
from PyQt5 import uic, QtWidgets, QtGui
import recursos_rc
qtCreatorFile = "PP1.ui"  # Nombre del archivo aquí.
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

        self.btn_aceptar.clicked.connect(self.Verificar)


        #label_2
        self.datosImagenes={
        0: [":/Logos/UAT.png", "UAT"],
        1: [":/Logos/Castor.jpg", "Castor programador"],
        2: [":/Logos/facultad_ingenieria_tampico.png", "La facultad de ingenieria..."],
        }
        self.cambiaValor()
        self.random()


    # Área de los Slots
    def cambiaValor(self):
        valor=self.selectorImagen.value()

        self.ruta_imagen = self.datosImagenes[valor][0]
        self.label_2.setPixmap(QtGui.QPixmap(self.ruta_imagen))

        #imagen_nombre = self.datosImagenes[valor][1]
        #self.txt_nombre_imagen.setText(imagen_nombre)

        #print(f"Imagen: {imagen_nombre}, Índice: {valor}")

    def Verificar(self):
        try:
            texto = self.txt_nombre_imagen.text()
            if self.ruta_imagen == texto:
                self.msj("Bien", "Es correcto")
                self.random()
            else:
                self.msj("Mal", "Es incorrecto")
        except error:
            print(error)


    def random(self):
        n = random.choice(list(self.datosImagenes.keys()))
        texto = self.datosImagenes[n][1]
        self.txt_nombre_imagen.setText(texto)
        self.selectorImagen.setValue(n)


    def msj(self, title, txt):
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