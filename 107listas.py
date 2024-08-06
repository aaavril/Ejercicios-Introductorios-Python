"""Ejercicio 5:
Matriz Transpuesta
Descripción del problema:
Escribe una función llamada matriz_transpuesta que tome una matriz representada como una
lista de listas y calcule su matriz transpuesta. La matriz transpuesta se obƟene intercambiando
filas por columnas, es decir, los elementos de la fila i en la matriz original se convierten en los
elementos de la columna i en la matriz transpuesta.
Ejemplo de entrada y salida:
matriz = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
matriz_transpuesta(matriz)
Salida:
[[1, 4, 7],
 [2, 5, 8],
 [3, 6, 9]] """

def matriz_transpuesta (matriz):
    filas= len(matriz)
    columnas = len(matriz[0])
    nueva_matriz= []

    for j in range(columnas):
        nueva_fila= []
        for i in range(filas):
            valor= matriz[i][j]
            nueva_fila.append(valor)
        nueva_matriz.append(nueva_fila)
    
    return nueva_matriz


matriz = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

print(matriz_transpuesta(matriz))
