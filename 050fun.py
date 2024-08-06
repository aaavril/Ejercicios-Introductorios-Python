'''12. Escribir una función que, dado una año, permita determinar si el mismo es 
bisiesto devolviendo True o False en caso contrario. Para esta función 
solo se utilizará una expresión lógica.
'''
def ano_bisiesto (ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

ano= int(input("Ingrese un año para saber si es o no bisiesto"))
print(ano_bisiesto(ano))
