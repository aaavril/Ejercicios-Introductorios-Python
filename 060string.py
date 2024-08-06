''' Realice lo mismo que en el ejercicio anterior, pero que escriba las letras del 
string en orden inverso (también una letra por línea). 
¿Puede implementar las dos versiones propuestas?'''

a= input ("Ingrese un string: ")
for i in range (len(a)-1, -1, -1):
    print (a[i])