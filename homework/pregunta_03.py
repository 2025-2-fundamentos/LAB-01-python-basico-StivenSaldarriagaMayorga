"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    data = open("files/input/data.csv", "r")
    tuplas = {}

    for line in data:
        letra = line.split()[0]
        if line.split()[0] in tuplas:
            tuplas[letra] += int(line.split()[1])
        else:
            tuplas[letra] = int(line.split()[1])
    
    a = sorted(list(tuplas.items()))
    return a

pregunta_03()
