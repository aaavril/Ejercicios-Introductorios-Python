'''Dadas 2 horas (horas, minutos y segundos) desarrollar una función 
para averiguar la diferencia en segundos de las 2 horas.

'''

def horario2segundos ():
    horas= int(input("Ingrese las horas: "))
    minutos= int(input("Ingrese los minutos: "))
    segundos= int(input("Ingrese los segundos: "))
    resultado_segundos= (horas*60*60)+(minutos*60)+(segundos)
    return resultado_segundos


resultado_segundos_1= horario2segundos ()
resultado_segundos_2= horario2segundos ()
diferencia_segundos= resultado_segundos_1 - resultado_segundos_2

print ("La diferencia de segundos entre los horarios es de", diferencia_segundos)