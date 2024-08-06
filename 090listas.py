"""Escribir una función que tenga como parámetro una lista con precios y devuelva el menor y el mayor de los precios."""

def menor_mayor (precios): #opción con max y min 
    maximo= max(precios)
    minimo= min(precios)
    return f"el mayor es {maximo}, y el menor es {minimo}"

def menor_mayor_recorriendo (precios): #función que hace lo mismo recorriendo
    maximo= precios[0]
    minimo= precios [0]
    for i in precios:
        if i < minimo:
            minimo= i
        elif i > maximo:
            maximo= i
    return f"el mayor es {maximo}, y el menor es {minimo}"

precios1= [123, 56, 2, 1000, 809]
print (menor_mayor (precios1))
print (menor_mayor_recorriendo (precios1))