'''Escribir un programa que tenga como parámetro el número correspondiente a la cantidad de sumas parciales 
(términos de la sumatoria) y que devuelva el valor correspondiente de la sumatoria hasta ese valor ingresado. 
¿conocen esta sumatoria? Prueben con varios números, ¿a qué les suena?:'''

def sumatoria (n):
    suma= 0 
    for i in range (n+1):
        termino= (1/16)**i * ((4/(8*i+1)) - (2/(8*i+4)) - (1/(8*i+5))- (1/(8*i+6)))
        suma += termino
    return suma

n1= int(input("Ingrese la cantidad de términos"))
print ("Sumatoria: ", sumatoria (n1))
