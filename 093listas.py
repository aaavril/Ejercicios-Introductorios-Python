"""4. Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo."""

import random

def crear_lista ():
    lista= []
    for i in range(10):
        n= random.randint(1,10) 
        lista.append(n)
    return lista
 

def imprimir_numeros (lista):
    for i in lista:
        print(i, i**2, i**3)

lista = crear_lista ()
imprimir_numeros (lista)



