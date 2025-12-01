"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():

    data = open("files/input/data.csv", "r")
    tuplas = {}

    for line in data:
        letra = line.split()[0]
        if line.split()[0] in tuplas:
            tuplas[letra] += 1
        else:
            tuplas[letra] = 1

    a = sorted(list(tuplas.items()))
    return a

pregunta_02()
