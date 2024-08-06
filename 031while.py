''' Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado.'''
numero= int(input("Ingrese numero positivos para descubrir el mayor, para terminar ingrese 0 "))
n_mayor= numero
while numero!=0:
    if numero>n_mayor:
        n_mayor= numero 
    numero= int(input("Ingrese numero positivos para descubrir el mayor, para terminar ingrese 0 "))
print("el mayor numero es ", n_mayor)
