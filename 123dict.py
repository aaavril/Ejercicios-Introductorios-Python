"""5. Escribir una función que quita los elementos duplicados de una lista 
utilizando un diccionario. Debe retornar una nueva lista sin elementos 
repetidos, sin importar el orden.
"""

def no_duplicados (lista):
    diccionario = dict()
    for i in lista:
        diccionario[i] = diccionario.get(i, 0) + 1
    for j in diccionario:
        if diccionario[j] > 1:
            del [j]
    resultado= diccionario.keys()
    resultado= list(resultado)
    return resultado

       
lista= [1, 2, 3, 4, 5, 1, 2, 3, 8, 8, 9, 2]   
print(no_duplicados(lista))
