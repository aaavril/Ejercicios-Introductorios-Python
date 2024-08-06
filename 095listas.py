"""Implementar una función que recibe una lista como parámetro y devuelve 
una nueva lista eliminando elementos duplicados."""

def lista_duplicados (lista):
    nueva_lista= []
    for i in lista:
        if i not in nueva_lista:
            nueva_lista.append(i)
    return nueva_lista

lista= [1, 2, 3, 4, 5, 6, 1, 2, 3]
print(lista_duplicados(lista))