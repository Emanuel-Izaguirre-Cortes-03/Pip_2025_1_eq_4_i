import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc
qtCreatorFile = "P16_CheckBox_Ejemplo1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.cb_supergucci.clicked.connect(self.streamer)
        self.cb_mrbeast.clicked.connect(self.streamer)
        self.cb_alka.clicked.connect(self.streamer)

        self.cb_pollo.toggled.connect(self.comida)
        self.cb_tacos.toggled.connect(self.comida)
        self.cb_pizza.toggled.connect(self.comida)


    # Área de los Slots
    def streamer(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Personaje: ",obj.text(), ":", valor)

    def comida(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Color: ",obj.text(), ":", valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())