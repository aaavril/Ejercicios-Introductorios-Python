"""Ejercicio 3: Producto Cartesiano de Listas
Escribe una función llamada producto_cartesiano que tome dos listas como entrada y calcule
su producto cartesiano. El producto cartesiano de dos listas A y B se define como un conjunto
de pares ordenados, donde el primer elemento del par proviene de la lista A y el segundo
elemento proviene de la lista B. Cada par posible debe estar presente en el producto
cartesiano.
lista1 = [1, 2, 3]
lista2 = ['rojo', 'verde']
producto_cartesiano[lista1, lista2]
Salida: [[1, 'rojo'], [1, 'verde'], [2, 'rojo'], [2, 'verde'], [3, 'rojo'], [3, 'verde']]Ejemplo de entrada y
salida:
lista1 = [1, 2]
lista2 = ['a', 'b']
producto_cartesiano(lista1, lista2)
Salida: [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
lista1 = [1, 2, 3]
lista2 = ['rojo', 'verde']
producto_cartesiano[lista1, lista2]
Salida: [[1, 'rojo'], [1, 'verde'], [2, 'rojo'], [2, 'verde'], [3, 'rojo'], [3, 'verde']] """


def producto_cartesiano(lista1, lista2):
    resultado = []
    len1 = len(lista1)
    len2 = len(lista2)
    for i in range(len1):
        for j in range(len2):
            resultado.append([lista1[i], lista2[j]])
    return resultado

lista1 = [1, 2, 3]
lista2 = ['rojo', 'verde']
print(producto_cartesiano(lista1, lista2))