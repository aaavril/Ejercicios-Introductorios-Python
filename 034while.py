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

ac1=0
ac2=0
ac3=0
ac4=0
ac5=0
ac6=0

for i in range(30):
    t1= random.randint(1,6)
    print (t1) 
    if t1==1:
       ac1= ac1 + 1
    elif t1== 2:
       ac2= ac2 + 1
    elif t1== 3:
       ac3= ac3 + 1
    elif t1== 4:
       ac4= ac4 + 1
    elif t1== 5:
       ac5= ac5 + 1
    elif t1== 6:
       ac6= ac6 + 1

print("La cara 1:", ac1, "\nLa cara 2:", ac2, "\nLa cara 3:", ac3, "\nLa cara 4:", ac4, "\nLa cara 5:", ac5, "\nLa cara 6:", ac6)
