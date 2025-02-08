import sys
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class DataAnalysisApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(DataAnalysisApp, self).__init__()
        loadUi("interfaz.ui", self)  # Carga el archivo de la interfaz generada con Qt Designer
        self.df = None  # Variable para almacenar los datos cargados

        # Conectar botones a sus funciones
        self.btnCargar.clicked.connect(self.cargar_datos)
        self.btnAnalizar.clicked.connect(self.analizar_datos)
        self.btnGuardar.clicked.connect(self.guardar_resultados)

    def cargar_datos(self):
        """Carga un archivo CSV y muestra los datos en la tabla"""
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Archivos CSV (*.csv);;Archivos de Texto (*.txt)")
        if archivo:
            try:
                self.df = pd.read_csv(archivo)  # Cargar datos en un DataFrame
                self.mostrar_datos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo: {str(e)}")

    def mostrar_datos(self):
        """Muestra los datos cargados en la tabla"""
        if self.df is not None:
            self.tablaDatos.setRowCount(self.df.shape[0])
            self.tablaDatos.setColumnCount(self.df.shape[1])
            self.tablaDatos.setHorizontalHeaderLabels(self.df.columns)

            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.tablaDatos.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.df.iat[i, j])))

    def analizar_datos(self):
        """Calcula y muestra estadísticas en el área de texto"""
        if self.df is None:
            QMessageBox.warning(self, "Advertencia", "No hay datos cargados para analizar.")
            return

        try:
            valores = self.df.select_dtypes(include=[np.number]).values.flatten()  # Seleccionar solo valores numéricos
            resultados = {
                "Valor Menor": np.min(valores),
                "Valor Mayor": np.max(valores),
                "Media": np.mean(valores),
                "Mediana": np.median(valores),
                "Moda": pd.Series(valores).mode()[0],
                "Desviación Estándar": np.std(valores),
                "Varianza": np.var(valores),
            }

            texto_resultados = "\n".join(f"{clave}: {valor}" for clave, valor in resultados.items())
            self.textResultados.setPlainText(texto_resultados)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Hubo un problema con el análisis: {str(e)}")

    def guardar_resultados(self):
        """Guarda los resultados del análisis en un archivo de texto"""
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivos de Texto (*.txt)")
        if archivo:
            try:
                with open(archivo, "w") as f:
                    f.write(self.textResultados.toPlainText())
                QMessageBox.information(self, "Éxito", "Resultados guardados correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = DataAnalysisApp()
    main.show()
    sys.exit(app.exec_())
