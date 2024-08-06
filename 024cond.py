'''Escribir un programa que permita determinar si un año es bisiesto utilizando la estructura condicional.'''

ano= int(input("Ingrese el año: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(ano, "es un año bisiesto.")
else:
    print(ano, "no es un año bisiesto.")