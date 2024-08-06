''' Escribir un programa que lea el día de la semana (en número entero, donde 1 corresponde a lunes y 7 a domingo) e imprima el siguiente mensaje:

-  si es lunes imprima “Hoy comienza la semana. Animo!”,

-  si es viernes “Ya casi termina!”

-  si es sábado o domingo “Siiii! Fin de semana!”

-  si el día ingresado no es ninguno de esos (pero es válido), imprimir el siguiente mensaje “Vamos que se puede!”

-  si el día ingresado no es válido entonces debe mostrar un cartel que lo indique'''

dia= int(input("Ingrese un día"))
if dia==1:
    print("Comienza la semana ¡Ánimo!")
elif dia==2 or dia==3 or dia==4:
    print("Vamos que se puede")
elif dia==5:
    print("Ya casi finde")
elif dia==6 or dia==7:
    print("Finde")
else:
    print("Error")
