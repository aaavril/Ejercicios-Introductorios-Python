"""Implementar una función Python que reciba una cadena por parámetro y busque en esa cadena 
las vocales y devuelva una tupla con la cantidad total de cada vocal, sin importar si las letras 
están en minúsculas o mayúsculas.
"""

def vocales(cadena):
    resultado= []
    cadena= cadena.lower()
    lista_cadena= list(cadena)
    vocales= ["a", "e", "i", "o", "u"]
    for i in range(len(vocales)):
            vocal= vocales[i]
            cuenta= lista_cadena.count(vocal)
            total= (vocal, cuenta)
            resultado.append(total)
    resultado= tuple(resultado)
    return(resultado)

    
print(vocales("Luna, perra del color azul JAJAJA"))

