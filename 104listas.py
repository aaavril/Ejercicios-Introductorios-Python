"""Ejercicio 2: Combinación de Listas
Descripción del problema:
Escribe una función llamada combinar_listas que tome dos listas como entrada y las combine
en una nueva lista de manera alternada. La nueva lista resultante debe contener elementos de
las listas originales en el siguiente orden: el primer elemento de la primera lista, el primer
elemento de la segunda lista, el segundo elemento de la primera lista, el segundo elemento de
la segunda lista, y así sucesivamente. Si una de las listas es más larga que la otra, los elementos
restantes deben agregarse al final de la lista resultante.
Ejemplo de entrada y salida:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd', 'e']
combinar_listas(lista1, lista2)
Salida: [1, 'a', 2, 'b', 3, 'c', 'd', 'e']
lista1 = ['rojo', 'verde']
lista2 = ['azul', 'amarillo', 'naranja']
combinar_listas(lista1, lista2)
Salida: ['rojo', 'azul', 'verde', 'amarillo', 'naranja']"""


def combinar_listas(lista1, lista2):
    resultado = []
    len1 = len(lista1)
    len2 = len(lista2)
    for i in range(max(len1, len2)):
        if i < len1:
            resultado.append(lista1[i])
        if i < len2:
            resultado.append(lista2[i])
    return resultado

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd', 'e']

combinadas = combinar_listas(lista1, lista2)
print(combinadas)