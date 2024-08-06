'''Dado el peso y altura de un adulto (peso en kilos y altura en centímetros), 
imprima por pantalla el nnúmero correspondiente al índice de masa corporal 
(solo el número, no la categoría).'''
altura= (float(input("Ingrese su altura en cm ")))
peso= (float(input("Ingrese su peso en Kg ")))
print("Su IMC es de ", (peso/(altura/100)**2))