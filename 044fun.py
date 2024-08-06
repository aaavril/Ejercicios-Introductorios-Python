'''Dada una hora (horas, minutos y segundos), desarrollar una función 
que devuelva la cantidad de segundos.

'''

def horario2segundos (horas, minutos, segundos):
    resultado_segundos= (horas*60*60)+(minutos*60)+(segundos)
    return resultado_segundos

horas= int(input("Ingrese las horas: "))
minutos= int(input("Ingrese los minutos: "))
segundos= int(input("Ingrese los segundos: "))

resultado_segundos_1= horario2segundos (horas, minutos, segundos)
print ("El resultado en segundos de el horario es de", resultado_segundos_1)