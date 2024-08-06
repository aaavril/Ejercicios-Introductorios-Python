"""7. Crear una función que permita determinar probabilísticamente resultados que se pueden obtener en 
una tirada de un dado. Para eso se deben generar 10.000 tiradas aleatorias y obtener el porcentaje que 
resulta para cada número posible en el dado.

La función debe devolver un diccionario como el siguiente: {1: 10, 2: 24, 3: 26, 4: 19, 5: 11, 6: 10} 
donde la clave corresponde al número de la cara del dado (1 a 6) y el valor al porcentaje de tiradas que 
salió dicho número (en este caso el 1 salió el 10% de las tiradas - 1000 tiradas- ).

"""
import random

def tirada_dados():
    #crear lista random de las 10.000 tiradas
    lista_resultados= []
    diccionario_resultados= {1:0, 2:0, 3:0, 4:0, 5:0}
    total= 10000
    for i in range(10000):
        n= random.randint(1,6)
        lista_resultados.append(n)
    for j in lista_resultados:
        diccionario_resultados[j] = diccionario_resultados.get(j, 0) + 1
    for k in diccionario_resultados:
        diccionario_resultados[k]= diccionario_resultados[k]/100
    return diccionario_resultados

print(tirada_dados())

