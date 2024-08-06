"""10.  Definir una función que recibe una cadena de caracteres  y cuente la cantidad de 
ocurrencias de cada letra del abecedario (sin distinguir mayúsculas de minúsculas).

Ejemplo:
funcion("06/2021: Ejercicios en Python.") 
--> { "E": 3, "J": 1, "R": 1, ... }  
"""

def contar_letras (cadena):
    #inicializar variables
    resultado= {}
    nueva_cadena= ""
    #pasar la cadena a mayúsculas
    cadena= cadena.upper()
    #recorrer la cadena para crear una nueva sin caractéres no alfabéticos
    for j in cadena:
        if j.isalpha():
            nueva_cadena += j
    #recorrer la cadena para agregar o actualizar el diccionario contando las letras4
    for i in nueva_cadena:
        print(i)
        if i not in resultado.keys():
            resultado.update({i: 1})
        else:
            resultado[i] = resultado.get(i) + 1
    return resultado

print(contar_letras("AEIOUaeiou"))

