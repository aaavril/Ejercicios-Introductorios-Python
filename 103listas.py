"""Ejercicio1: Comprimir Lista de Números
Descripción del problema:
Escribe una función llamada comprimir_lista que tome una lista de números como entrada y
devuelva una nueva lista que comprima las secuencias de números repeƟdos. En la lista
resultante, cada secuencia de números repeƟdos debe ser reemplazada por un par [valor,
canƟdad], donde "valor" es el número repeƟdo y "canƟdad" es el número de veces que se
repite consecuƟvamente.
Ejemplo de entrada y salida:
numeros = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5]
comprimir_lista(numeros)
Salida: [[1, 3], [2, 2], 3,[4, 2], [5, 4]]
numeros = [2, 2, 2, 2, 2, 2, 2]
comprimir_lista(numeros)
Salida: [[2, 7]]
numeros = [1, 2, 3, 4, 5]
comprimir_lista(numeros)
Salida: [1, 2, 3, 4, 5]Ten en cuenta que en la salida, los pares [valor, canƟdad]. """

def comprimir_lista(numeros):
    numeros_contados= []
    numeros_una_vez= []
    for i in numeros:
        if i not in numeros_contados:
            veces= numeros.count(i)
            lista= [i, veces]
            numeros_contados.append(lista)
    for i in numeros_contados:
        if i not in numeros_una_vez:
            numeros_una_vez.append(i)
    for k in range(len(numeros_una_vez)):
        if numeros_una_vez[k][1] == 1:
            numeros_una_vez[k]= numeros_una_vez[k][0]
    return numeros_una_vez


numeros1 = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5]
print(comprimir_lista(numeros1)) #Salida: [[1, 3], [2, 2], 3,[4, 2], [5, 4]]

numeros2 = [2, 2, 2, 2, 2, 2, 2]
print(comprimir_lista(numeros2)) #Salida: [[2, 7]]

numeros3 = [1, 2, 3, 4, 5]
print(comprimir_lista(numeros3)) #Salida: [1, 2, 3, 4, 5]