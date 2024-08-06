"""Ejercicio 4: Matriz de MulƟplicación
Descripción del problema:
Escribe una función llamada matriz_mulƟplicacion que tome dos matrices representadas como
listas de listas y calcule su mulƟplicación. La mulƟplicación de dos matrices se realiza
mulƟplicando cada elemento de una fila de la primera matriz por cada elemento de una
columna de la segunda matriz y sumando los resultados para obtener el elemento
correspondiente de la matriz resultante.
Ejemplo de entrada y salida:
matriz1 = [[1, 2, 3],
 [4, 5, 6]]
matriz2 = [[7, 8],
 [9, 10],
 [11, 12]]

matriz_mulƟplicacion(matriz1, matriz2)
Salida:
[[58, 64],
 [139, 154]]"""

def matriz_multiplicacion(matriz_a, matriz_b):

    # Suponemos que las dimensiones de las matrices son compatibles

    # Obtenemos las dimensiones de las matrices
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])

    # Inicializamos la matriz de resultado como una lista vacía
    resultado = []

    # Realizamos la multiplicación de matrices
    for i in range(filas_a):
        nueva_fila = []
        for j in range(columnas_b):
            suma = 0
            for k in range(columnas_a):
                suma = suma + matriz_a[i][k] * matriz_b[k][j]
            nueva_fila.append(suma)
        resultado.append(nueva_fila)

    return resultado


matriz_a = [[1, 2, 3], [4, 5, 6] ]
matriz_b = [[7, 8], [9, 10], [11, 12]]

resultado = matriz_multiplicacion(matriz_a, matriz_b)
print(resultado)