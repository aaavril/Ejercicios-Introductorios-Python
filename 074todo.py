"""Escribir la función fizzbuzz(numero), que recibe un número natural que retornara:
fizzbuzz si el número es divisible entre 3 y 5 a la vez.
fizz si el número es divisible entre 3
buzz si el número es divisible entre 5
el propio número (como string) si no es divisible entre 3 ni entre 5
Utilizar la función en un programa donde pidan un número entre 1 y 100 e imprimir el resultado de la
función para dicho número.
"""

def fizzbuzz (numero):
    if numero%3==0 and numero%5==0:
        cadena= "fizzbuzz"
    elif numero%3==0:
        cadena= "fizz"
    elif numero%5==0:
        cadena= "buzz"
    else:
        cadena= (str(numero))
    return cadena


numero1= int(input("Ingrese un número entre 1 y 100: "))
if numero1>100 or numero1<1:
    while numero1>100 or numero1<1:
        numero1= int(input("Ingrese un número entre 1 y 100: "))
print (fizzbuzz (numero1))
