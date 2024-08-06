'''Se desea calcular la distancia recorrida por un automóvil que tiene una velocidad
constante expresada en km/h durante un tiempo t (en segundos). La distancia recorrida debe expresarse en metros.'''
velocidad=(float(input("Ingrese la velocidad del automóvil en km/h")))
velocidad= velocidad/3.6
tiempo=(float(input("Ingrese el tiempo del automóvil en segundos")))
print ("La distancia recorrida por el automóvil es de ", velocidad*tiempo, "metros")