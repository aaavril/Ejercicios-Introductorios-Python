'''11. Escribir una función que realice el cálculo de ambas raíces 
reales (asumiendo que las tiene) de un polinomio de segundo grado y que imprima 
en pantalla ambas raíces. Los parámetros de la función son los coeficientes del polinomio 
a, b, y c. ¿Qué pasa cuando el determinante es menor que 0? 
'''
'''
'''

from math import sqrt

def calculo_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        resultado = "El polinomio no tiene raíces reales."
    else:
        x1 = (-b + sqrt(discriminante)) / (2*a)
        x2 = (-b - sqrt(discriminante)) / (2*a)
        if x1 == x2:
            resultado = f"El polinomio tiene raíces dobles que son: {x1} y {x2}"
        else:
            resultado = f"El polinomio tiene raíces reales que son: {x1} y {x2}"
    return resultado

a1 = float(input("Ingrese el coeficiente del término en grado 2: "))
b1 = float(input("Ingrese el coeficiente del término en grado 1: "))
c1 = float(input("Ingrese el coeficiente del término independiente: "))

print (calculo_raices(a1, b1, c1))