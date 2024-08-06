'''Escribir un programa que implemente el valor absoluto (pero sin usar la función provista por python). 
Nota: para los números positivos su valor absoluto es igual al número (ej: el valor absoluto de 52 es 52), 
mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 
(el valor absoluto de -52 es 52).'''

numero= int(input("ingrese un número"))
if numero<0:
    numero_convertido= numero*(-1)
else:
    numero_convertido= numero

print(numero_convertido)