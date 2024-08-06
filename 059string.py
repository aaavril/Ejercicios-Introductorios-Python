'''1. Escriba un programa en Python donde el usuario ingrese un 
string por teclado y luego imprima todas sus letras (una en cada fila). 
Realíce una versión iterando sobre las letras del string y otra iterando 
sobre los índices de las letras (es decir, usando for-range). Ej: si el 
string ingresado es auto deberá escribir:

a
u
t
o'''

a= input ("Ingrese un string: ")

"""
opción más fácil
for i in a:
    print (i)
"""

for i in range(len(a)):
    print (a[i]) #el string tiene un indice, auqnue no podemos modificar tiene indice que empieza en 0, esto te deja acceder a la letra en esa posición. 