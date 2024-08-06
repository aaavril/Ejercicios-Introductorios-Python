'''Escriba la función “formateanombre” que reciba como parámetros de entrada el nombre, 
el apellido (strings) y el número de cédula (número entero) y devuelva un string con 
la siguiente frase: apellido, nombre tiene el número de cédula número'''

def formateanombre (nombre, apellido, cedula):
    frase_formateada= f"{apellido}, {nombre} tiene el número de cédula {cedula}"
    return frase_formateada

nombre= str(input("ingrese su nombre: "))
apellido= str(input("ingrese su nombre: "))
cedula= str(input("ingrese su número de cédula: "))

frase_formateada1= formateanombre(nombre, apellido, cedula)
print (frase_formateada1)