"""Dos números enteros son primos entre sí (también llamados coprimos o primos relativos) si únicamente
tienen 1 (y - 1) como divisor común, es decir que no tienen ningún factor primo en común. Por ejemplo, 6 y
19 son coprimos, pero 6 y 27 no lo son porque ambos son divisibles por 3.
Implemente la función: coprimos(a, b), donde a y b son números enteros positivos, debe retornar True
si los números son coprimos y False en caso contrario.
"""

def coprimos(a, b):
    if a > b:
        aux = b
        b = a
        a = aux
    son_coprimos = True
    divisor = 2
    while divisor < a:
        if a % divisor == 0 and b % divisor == 0:
            son_coprimos = False
        divisor = divisor + 1
    return son_coprimos

# Programa principal
a = int(input("Ingrese primer número entero positivo : "))
b = int(input("Ingrese segundo número entero positivo: "))
if coprimos(a, b):
    print(f"Los números {a} y {b} son co-primos")
else:
    print(f"Los números {a} y {b} NO son co-primos")