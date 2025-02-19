import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P04_EjemploSpinBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.spinBox.valueChanged.connect(self.cambiaValor)
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(2)
        self.spinBox.setValue(0)

    # Área de los Slots
    def cambiaValor(self):
        valor=str(self.spinBox.value())
        self.lineEdit.setText(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())