import sys
from PyQt5 import uic, QtWidgets
import Recursos_rc
qtCreatorFile = "P14_RadioButton_Ejemplo2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.rb_batman.clicked.connect(self.batman)
        self.rb_john.clicked.connect(self.john)

        self.rb_azul.toggled.connect(self.azul)
        self.rb_rojo.toggled.connect(self.rojo)


    # Área de los Slots
    def batman(self):
        valor=self.rb_batman.isChecked()
        print("Batman: ",valor)

    def john(self):
        valor=self.rb_john.isChecked()
        print("John: ",valor)

    def azul(self):
        valor=self.rb_azul.isChecked()
        if valor:
             print("Azul: ",valor)

    def rojo(self):
        valor=self.rb_rojo.isChecked()
        if valor:
             print("Rojo: ",valor)

    def verde(self):
        valor=self.rb_verde.isChecked()
        if valor:
             print("Verde: ",valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())