'''Escribir un programa que realice el cálculo de ambas raíces reales 
(asumiendo que las tiene) de un polinomio de segundo grado y que imprima 
en pantalla ambas raíces. No realice ningún control sobre el discriminante. 
¿Qué sucede en la ejecución del programa si el discriminante es menor a cero?'''
import math
a=(float(input("Ingrese el coeficiente del término en grado 2 ")))
b=(float(input("Ingrese el coeficiente del término en grado 1 ")))
c=(float(input("Ingrese el coeficiente del término independiente ")))
x1=(float(-b + math.sqrt(b**2 - 4*a*c)) / (2*a))
x2=(float(-b - math.sqrt(b**2 - 4*a*c)) / (2*a))
print ("Las raíces del polinomio son: ", x1 , " y ", x2)
#me da error porque si el discriminante es negativo tendría que hacer otra cosa