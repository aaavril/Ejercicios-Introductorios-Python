"""Ejercicio 4
Escribir una función que devuelve True si el argumento (un string) es capicúa, es decir que es igual leerlo
de izquierda a derecha o de derecha a izquierda (False en caso contrario). Tener en cuenta que las letras
con acento también pueden admitirse .
Ej: "neuquén", "reconocer" son palabras capicúa.
"""

def remover_acentos(cadena):
    conversión={"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    salida=""
    for caracter in cadena:
        salida=salida+conversión.get(caracter, caracter)
    return salida

def capicua (cadena):
    cadena= remover_acentos(cadena)
    lista= list(cadena)
    lista_revertida= lista[::-1]
    if lista == lista_revertida:
        resultado= True
    else:
        resultado= False
    return resultado

print(capicua("reconocer"))

