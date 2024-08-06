"""Escribir una función que calcule (devuelva) el desvío estándar de un conjunto de n números reales positivos.
Los números se irán ingresando por teclado; cuando se ingrese un número negativo se indicará que se han
dejado de ingresar (el número negativo no formará parte del cálculo, solo los anteriores). La desviación
estándar de un conjunto de números x~1~, x~2~, ..., x~n~ es la raíz cuadrada de la expresión s/n - a^2^
ejercicios-preparacion-parcial2.md 2023-10-16
4 / 6
donde a es el promedio de los valores x~i~ (es decir, [(x~1~+x~2~+ ... +x~n~) / n]) y s es la suma de los
cuadrados de los valores x~i~(es decir, x~1~^2^ + x~2~^2^ + ... + x~n~^2^).
Ejemplo:
Si la entrada es: 25.0 23.0 22.0 21.0 17.0 9.0 6.0 5.0 -1.0, la función devolverá 7.60
"""

import math
def calcula_desvio_estandar():
    s = 0
    suma = 0
    n = 0
    x = float(input("Ingrese un valor: "))
    while x >= 0:
        s += x**2
        suma += x
        n += 1
        x = float(input("Ingrese un valor: "))
    a = suma / n
    return round(math.sqrt(s/n - a**2),2)

desvio_estandar = calcula_desvio_estandar()
print()
print(f"El desvio estandar es: {desvio_estandar}")
print()