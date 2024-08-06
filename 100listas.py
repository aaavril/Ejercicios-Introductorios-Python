"""DESAFÍO 3: LOTERÍA
2. Definir una función que permita generar un cartón de lotería. Un cartón de lotería contiene 3 
filas con 5 números cada una. Los números son aleatorio entre 1 y 99 y no se repiten. 
La función debe retornar una lista conteniendo las 3 filas, es decir 3 listas, con 5 números.

Ej: generar_carton() -> [[13,10,11,16,15],[1,8,62,36,45],[99,97,85,73,28]]

"""

import random

def generador_filas():
    fila= []
    for i in range(5):
        n= random.randint(1, 99)
        fila.append(n)
    return fila

def carton():
    carton= []
    for i in range(3):
        carton.append(generador_filas())
    return carton 

print(carton())

