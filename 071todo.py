"""
Escriba la función pertenece_al_intervalo que reciba como parámetros tres números: n,
limite_inferior, limite_superior. Esta función debe retornar verdadero o falso si
limite_inferior <= n <= limite_superior (es decir, si n está entre limite_inferior y
limite_superior).
NOTA: para esto tenga en cuenta que la función retornará un valor True o False , es decir un tipo de dato
booleano.
Prueba la función con el siguiente programa:"""


def pertenece_al_intervalo(N, linf, lsup):
    return linf <= N and N <= lsup

N1 = float(input("Ingrese un número: "))
linf1 = float(input("Ingrese un límite inferior: "))
lsup1 = float(input("Ingrese un límite superior: "))
if pertenece_al_intervalo(N1, linf1, lsup1):
    print("el número pertenece al intervalo")
else:
    print("el número no pertenece al intervalo")