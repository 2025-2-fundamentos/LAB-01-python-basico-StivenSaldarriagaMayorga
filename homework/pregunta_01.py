"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():

    data = open("files/input/data.csv", "r")
    total = 0
    for line in data:
        total += int(line[2]) 
    print(total)
    return total

pregunta_01()
