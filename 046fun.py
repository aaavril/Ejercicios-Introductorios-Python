'''Escribir una función que dibuja un rectángulo en pantalla utilizando 
el caracter “x”. El tamaño del rectángulo está dado por la cantidad de “x” 
en la base y en la altura.
'''
def rectangulo ():
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

rectangulo ()