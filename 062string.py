'''Escribir una función que recibe una cadena de caracteres como 
parámetros con una fecha de la forma “dd/mm/aaaa” y devuelve 
la fecha en formato “aaaa­‐ mm­‐dd”.

Ej.: 10/11/1977 ->1977­‐11­‐10

NOTA: No se debe utilizar la función split de Python.'''

def funcion_fecha (fecha):
    dd= fecha[:2]
    mm= fecha[3:5]
    aaaa= fecha[6:]
    return (f"{aaaa}-{mm}-{dd}")

print(funcion_fecha("28/12/2005"))