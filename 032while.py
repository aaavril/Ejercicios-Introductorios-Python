'''Escribir un programa que dibuja un rectángulo en pantalla utilizando el caracter “x”. El tamaño del rectángulo 
está dado por la cantidad de “x” en la base y en la altura.

Ej.: si se ingresa 7 y 5 como entrada, imprime:

xxxxxxx 
x     x
x     x
x     x
xxxxxxx 


base= int(input("Ingrese el tamaño de la base del rectángulo"))
altura= int(input("Ingrese el tamaño de la altura del rectángulo"))
print("x"*base)
while (altura-2)>0:
    print("x"+" "*(base-2)+"x")
    altura= altura-1
print("x"*base)

'''

base= int(input("Ingrese el tamaño de la base del rectángulo"))
altura= int(input("Ingrese el tamaño de la altura del rectángulo"))
if base==1 and altura==1:
    print ("x")
elif base==2 and altura==1:
    print ("xx")
elif base==0 or altura==0:
    print ("error")
else: 
    print("x"*base)
    i=0
    while i< altura-2:
        print("x"+" "*(base-2)+"x")
        i=i+1
    print( "x"* base)

