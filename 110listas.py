"""Ejercicio 8:
Triángulo de Pascal
Descripción del problema:
El Triángulo de Pascal es un triángulo numérico que se construye con la siguiente regla: cada
número en el triángulo es la suma de los dos números que se encuentran justo encima de él en
el triángulo. Los bordes del triángulo conƟenen solo unos (1) y cada número interno es la suma
de los dos números superiores.
Escribe una función llamada triangulo_pascal que tome un número entero n como entrada y
genere las primeras n filas del Triángulo de Pascal. La función debe devolver una lista de listas,
donde cada lista interna representa una fila del triángulo.
Ejemplo de entrada y salida:
triangulo_pascal(5)
Salida:
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
triangulo_pascal(7)

Salida:
[ [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1],
 [1, 5, 10, 10, 5, 1],
 [1, 6, 15, 20, 15, 6, 1]] """

def triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    return triangulo

print(triangulo_pascal(5))
print(triangulo_pascal(10))

