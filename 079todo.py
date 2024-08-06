"""Escribir un programa donde el usuario pueda ingresar por teclado tres números naturales x, a, b. El
programa deberá mostrar por pantalla todos los múltiplos de x que aparecen entre a y b (a y b incluidos).
Ejemplo: si x=3, a = 3 y b = 20 imprime los números 3, 6, 9, 12, 15, 18
Si no recuerdas cómo se define el múltiplo de un número:"""

def multiplos(x, a, b):
    n = 1
    multiplo = x
    while multiplo <= b:
        multiplo = x * n
        if (multiplo >= a and multiplo <= b):
            print(multiplo)
        n = n + 1
        
multiplos(3, 3, 20)