"""Dados dos números positivos N y D, se dice que D es un divisor de N si el resto de dividir N entre D es 0. Se
dice que un número es perfecto si la suma de sus divisores (excluido el propio N) es N. Por ejemplo 28 es un
número perfecto, pues sus divisores (excluido el 28) son: 1, 2, 4, 7 y 14, la suma de los divisores es:
1+2+4+7+14 = 28.
Escribir una función es_perfecto(N), que retorne True si N es un número perfecto y retorne False en
caso contrario.
Utilice la función en un programa que pida dos números positivos a y b, siendo a < b, e imprima la
cantidad de números perfectos entre esos dos números (incluidos).
"""

def ingreso_positivo(mensaje):
    num = int(input(mensaje))
    while num <= 0:
        num = int(input(mensaje))
    return num

def es_perfecto(n):
    suma = 0
    d = 1
    while d < n:
        if n % d == 0:
            suma = suma + d
        d = d + 1
    return suma == n

numero_a = ingreso_positivo("Ingrese el primer número positivo (mayor que cero) : ")
numero_b = ingreso_positivo("Ingrese el segundo número positivo (mayor que cero): ")
while numero_a <= numero_b:
    if es_perfecto(numero_a):
        print(numero_a)
    numero_a = numero_a + 1
