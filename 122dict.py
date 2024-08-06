"""4. Escribir un programa que permite realizar una estadística de los nombres que 
llevan los recién nacidos. El programa deberá llevar registro de cada nombre y la 
cantidad de niños/niñas que lo llevan (solo primer nombre).  Para eso solicitará al 
usuario que ingrese los nombres por pantalla uno a la vez. Para finalizar, ingresa 
la cadena vacía y el programa muestra una lista con los nombres y la cantidad de niños con ese nombre.
"""

nombres= {}
nombre= input("Ingrese un nuevo nombre: ")
while nombre != "":
    if nombre in nombres:
        nombres[nombre]+= 1
    else:
        nombres[nombre]= 1
    nombre= input("Ingrese un nuevo nombre: ")

for n in nombres.keys():
    print (n, nombres[n])
