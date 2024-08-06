'''Extra 1
Parte 1
Crea una función que reciba un número y dos cadenas de texto e imprima:
- Si el número es múltiplo de 3, imprima la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, imprima la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, imprima las dos cadenas de texto concatenadas. '''


'''def texto (n1, c1, c2):
    if n1%3==0 and n1%5==0:
        resultado= c1+c2
    elif n1%3==0:
        resultado= c1
    elif n1%5==0:
        resultado= c2
    return resultado

n1= int(input("Ingrese un número: "))
c1= input("ingrese una cadena de texto")
c2= input("ingrese otra cadena de texto")
print (texto (n1, c1, c2))'''

'''Parte 2
 - Solicitar un número N, y desde 1 hasta N imprimir: 
- Si el número es múltiplo de 3, imprima la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, imprima la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, imprima las dos cadenas de texto concatenadas.
'''

def texto (n1, c1, c2):
    for i in range (1, n1+1):
        if i%3==0 and i%5==0:
            print (c1+c2)
        elif i%3==0:
            print (c1)
        elif i%5==0:
            print (c2)


texto (15, "mult 3", "mult 5")
