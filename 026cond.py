'''9. Escribir el mismo programa anterior pero el día 
de la semana se especifica con string (es decir el input leerá 
el día de la semana en letras, por ejemplo “lunes”).
 Tenga en cuenta que algunos controles podrían cambiar.'''

dia= input("Ingrese un día de la semana")
if dia=="lunes" or dia=="Lunes":
    print("Comienza la semana ¡Ánimo!")
elif dia=="martes" or dia=="martes" or dia=="miércoles" or dia=="Miércoles" or dia=="jueves" or dia=="Jueves":
    print("Vamos que se puede")
elif dia=="viernes" or dia=="Viernes":
    print("Ya casi finde")
elif dia=="sábado" or dia=="Sábado" or dia=="Domingo" or dia=="domingo":
    print("Finde")
else:
    print("Error")