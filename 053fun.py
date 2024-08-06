'''15. Escribir un programa que indique si un número es de buena suerte o no 
(un número es de buena suerte si sus dígitos suman 21). Observe que puede reutilizar 
inteligentemente el ejercicio anterior.
'''
def ultimodigito(n):
    ult = n % 10 
    return ult

def sacarultimodigito(n):
    n_sin_ult = n // 10 
    return n_sin_ult

n = int(input("Ingrese un número: "))
suma = 0

while n >= 1:
    ultimo = ultimodigito(n)
    suma += ultimo
    n = sacarultimodigito(n)

if suma==21:
    print("Este es un número de la suerte")
else:
    print("Este no es un número de la suerte")
