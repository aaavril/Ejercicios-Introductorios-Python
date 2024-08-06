'''Escribir un programa que, dados dos números que se leen por teclado imprime "Verdadero" si 
el resultado de multiplicar ambos números es 1 y "Falso" si no lo son. Ej.: 2 y 0.5, 5 y 0.2, 2.5 y 0.4.'''

n1= float(input("ingrese un numero: "))
n2= float(input("ingrese otro numero para saber si multiplican 1: "))
if n1*n2==1:
    print("verdadero")
else:
    print("falso")
