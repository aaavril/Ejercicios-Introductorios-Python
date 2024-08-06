"""Ejercicio 6
Implementar en Python una función que recibe como parámetro una lista de números de cédulas de
identidad de las personas que fueran vacunadas en un centro de vacunación COVID. Cada vez que aparece
una cédula en esa lista, significa que se registró una dosis recibida por la persona (es decir, si en la lista una
cédula x aparece 2 veces, significa que esa persona recibió dos dosis). La función debe construir un
diccionario en el que, para cada cédula, almacene la cantidad de dosis recibidas y devolver una lista de los
números de cédula que han recibido 3 o más dosis .
"""

def dosis(listacedulas):
    lista3dosis = []
    dicc = {}
    for cedula in listacedulas:
        dicc[cedula] = dicc.get(cedula, 0) + 1
    for clave in dicc.keys():
        if dicc[clave]>=3:
            lista3dosis.append(clave)
    return lista3dosis


print(dosis([1,2,3,4,5,2,6,7,2,3,8,3,1,6,7,7]))