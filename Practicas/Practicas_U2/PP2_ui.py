from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Botón para iniciar el temporizador
        self.btn_temporizador = QtWidgets.QPushButton(self.centralwidget)
        self.btn_temporizador.setGeometry(QtCore.QRect(150, 100, 100, 30))
        self.btn_temporizador.setObjectName("btn_temporizador")

        # Etiqueta para mostrar el tiempo transcurrido
        self.label_tiempo = QtWidgets.QLabel(self.centralwidget)
        self.label_tiempo.setGeometry(QtCore.QRect(150, 150, 100, 30))
        self.label_tiempo.setObjectName("label_tiempo")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temporizador"))
        self.btn_temporizador.setText(_translate("MainWindow", "Iniciar"))
        self.label_tiempo.setText(_translate("MainWindow", "Tiempo: 0 s"))
