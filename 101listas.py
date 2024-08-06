"""DESAFÍO 3: EDITOR DE TEXTO
Crear un programa que solicita al usuario oraciones y le permite cargarlas en una lista 
(cada oración es un elemento de la lista).


Cada oración deberá comenzar con la primera letra en mayúscula y finalizar en punto. 
En caso que el usuario lo ingrese de otra forma, el programa deberá corregir la oración automáticamente.

Se deberán admitir líneas en blanco.

El programa finaliza cuando el usuario ingresa únicamente la cadena de caracteres “::q” (dos puntos, dos puntos, letra q)

Al finalizar debe mostrar, todas la oraciones y una estadística con la cantidad de oraciones ingresadas y 
la cantidad de caracteres totales (incluyendo caracteres en blanco, símbolos y caracteres de control)."""

lista= []
continuar= True
contador= 0
caracteres= 0

while continuar == True:
    oracion= input("Ingrese una oración. Ingrese “::q” (dos puntos, dos puntos, letra q) para finalizar el programa: ")
    if oracion == "::q":
        continuar= False 
    else:
       oracion= oracion.capitalize()
       if oracion[-1]!= ".":
           oracion= oracion+"."
       lista.append(oracion)
       caracteres+= len(oracion)
       contador += 1

print(f"Se ingresaron {contador} oraciones, el total de caracteres es de {caracteres}, \ny las oraciones ingresadas fueron las siguientes: ")
for i in lista:
    print(i)


