import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E04_Áreas de un pentágono.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_sumar.clicked.connect(self.suma)

    # Área de los Slots
    def suma(self):
        try:
            num1 = float(self.txt_A.text())
            num2 = float(self.txt_B.text())
            num1 = num1 * 5
            sum = num1 * num2 /2
            self.msj("El area es de: " + str(sum) + " cm2")
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

