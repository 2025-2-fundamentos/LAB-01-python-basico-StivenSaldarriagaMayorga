"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data = open("files/input/data.csv", "r")
    tuplas = {}

    for line in data:
        columnas = line.split()
        valor = int(columnas[1])
        col4 = columnas[3].split(",")
        for letra in col4:
            tuplas[letra] = tuplas.get(letra, 0) + valor

    return dict(sorted(tuplas.items()))