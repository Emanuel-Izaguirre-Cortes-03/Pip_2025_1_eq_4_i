import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc
qtCreatorFile = "P15_RadioButton_Ejemplo3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.rb_batman.clicked.connect(self.personaje)
        self.rb_john.clicked.connect(self.personaje)
        self.rb_iron.clicked.connect(self.personaje)

        self.rb_azul.toggled.connect(self.color)
        self.rb_rojo.toggled.connect(self.color)
        self.rb_verde.toggled.connect(self.color)


    # Área de los Slots
    def personaje(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Personaje: ",obj.text(), ":", valor)

    def color(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Color: ",obj.text(), ":", valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())