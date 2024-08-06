''' Escriba un programa que reciba como entrada la edad de una persona y el nombre y genere un string. 
Si la edad es menor a 18 años el string debería ser “nombre, eres menor de edad” 
(obviamente nombre será reemplazado por el nombre de la persona); 
en caso contrarío, el string será “nombre, ya eres mayor de edad”. Imprima luego ese string'''
nombre= input("Ingrese su nombre ")
edad= int(input("Ingrese su edad "))
if edad>=18:
    mayormenor= "mayor"
else: 
    mayormenor= "menor"
print(nombre, "eres ", mayormenor, " de edad."