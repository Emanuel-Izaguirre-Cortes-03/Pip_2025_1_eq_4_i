from matplotlib import pyplot as plt

archivo=open("../Archivos/Calificaciones_Concentrado.csv")
contenido=archivo.readlines()
print(contenido)

datos=[]
for linea in contenido:
    datos.append(linea.split(","))
print(datos)

datosT=[]
for registro in datos:
    temporal=[registro[0], list(map(int,registro[1:]))]
    datosT.append(temporal)
print(datosT)

for registro in datosT:
    registro.append(sum(registro[1])/len(registro[1]))
print(datosT)

nombres=[i[0] for i in datosT]
promedios=[i[2] for i in datosT]

print(nombres)
print(promedios)

plt.bar(nombres,promedios)
plt.show()