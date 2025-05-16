import numpy as np

archivo = open("Instancia_paraDividir.txt")
contenido = archivo.readlines()

X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(float, i)) for i in X]

Y = contenido[3+int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(float, i)) for i in Y]

X = np.array(X)
Y = np.array(Y)

print("X:")
print(X)

print("Y:")
print(Y)

print("Elementos X: ", X.shape)
print("Elementos Y: ", Y.shape)

factorEntrenamiento = 0.8 #80% del total de elementos
regEntrenamiento = int(factorEntrenamiento * X.shape[1])
regPrueba = X.shape[1] - regEntrenamiento
print("Registros para entrenamiento: ", regEntrenamiento)
print("Registros para prueba: ", regPrueba)
posSeleccionadas = []
datosEntrenamientoX = []
datosEntrenamientoY = []
import random as rnd
for i in range(regEntrenamiento):
    index = rnd.randint(0, regEntrenamiento-1)
    while index in posSeleccionadas:
        index = rnd.randint(0, regEntrenamiento - 1)
    datosEntrenamientoY.append([
        Y[0][index],
        Y[1][index],
        Y[2][index]
    ])
    datosEntrenamientoX.append([
            X[0][index],
            X[1][index],
            X[2][index],
            X[3][index]
        ])
    posSeleccionadas.append(index)

print()