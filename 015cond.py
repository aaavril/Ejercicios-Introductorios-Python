'''Encontrar las raíces de un polinomio de segundo grado mediante un algoritmo
expresado en pseudocódigo. El programa debe indicar si no tiene raíces reales, si
tiene raíces dobles (y su valores) o si tiene dos raíces reales (y su valores).'''

import math
a=(float(input("Ingrese el coeficiente del término en grado 2 ")))
b=(float(input("Ingrese el coeficiente del término en grado 1 ")))
c=(float(input("Ingrese el coeficiente del término independiente ")))
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("El polinomio no tiene raíces reales.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    if x1==x2:
        print("El polinomio tiene raíces dobles que son:", x1 , "y", x2)
    else:
        print("El polinomio tiene dos raíces reales que son:", x1, "y", x2)