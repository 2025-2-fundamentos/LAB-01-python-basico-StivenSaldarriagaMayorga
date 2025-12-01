"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    data = open("files/input/data.csv", "r")
    lista = []
    tuplas = {}

    for line in data:
        letra = line.split()[0]
        numero = int(line.split()[1])
        if letra in tuplas:
            tuplas[letra][1] = max(tuplas[letra][1], numero)
            tuplas[letra][2] = min(tuplas[letra][2], numero)
        else:
            tuplas[letra] = [letra, numero, numero]

    for clave in tuplas:
        lista.append(tuple(tuplas[clave]))
            
    return sorted(lista)

