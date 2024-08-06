'''Como hemos visto en el curso, en Python muchas funciones están implementadas en módulos que son 
archivos conteniendo definiciones con código fuente Python. Para utilizar un módulo es necesario
 importar el módulo mediante la declaración “import” seguido del nombre del módulo.


El módulo “random” contiene la función random.randint donde random.randint(1,6) 
devuelve un número aleatorio entre 1 y 6 (incluidos) y que se puede utilizar para
 simular la tirada de un dado.

a)    Realizar un programa para simular 20 tiradas de dos dados simultáneamente, 
dando el promedio de la suma de los resultados de los dos dados.

b)    Realizar un programa que cuente la cantidad de veces que salió la 
cara 1, 2, … 6 en 30 tiradas.'''

import random

acumulador=0
for i in range(20):
    t1= random.randint(1,6) 
    t2= random.randint(1,6)
    promediotirada= (t1+t2)/2
    acumulador= acumulador + promediotirada
print (acumulador)

