'''Escribir un algoritmo que dado un número de 5 dígitos determine si es capicúa o no.'''

numero = input("Ingrese un número de 5 dígitos: ")
num_revertido = numero[::-1]
if numero == num_revertido:
    print("El número", numero, "es capicúa.")
else:
    print("El número", numero, "no es capicúa.")


