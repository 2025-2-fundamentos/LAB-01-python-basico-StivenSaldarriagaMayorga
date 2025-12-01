"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    data = open("files/input/data.csv", "r")
    tuplas = {}

    for line in data:
        posicion = line.split()
        clave_tres_letras = posicion[4].split(",")

        for values in clave_tres_letras:
            clave, valor = values.split(":")
            valor = int(valor)

            if clave not in tuplas:
                
                tuplas[clave] = [valor, valor]
            else:
                
                tuplas[clave][0] = min(tuplas[clave][0], valor)
                tuplas[clave][1] = max(tuplas[clave][1], valor)

    a = sorted((c, v[0], v[1]) for c, v in tuplas.items())
    return a

