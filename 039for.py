''' Escribir un programa que solicite al usuario una cantidad y luego itere 
la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un número. 
Al finalizar, mostrar la suma de todos los números ingresados.'''

veces= int(input("ingrese la cantidad de veces que quiere iterar la suma"))
suma=0

for i in range(veces):
    n= int(input("Ingrese un número para sumar"))
    suma= suma+n 

print (suma)

