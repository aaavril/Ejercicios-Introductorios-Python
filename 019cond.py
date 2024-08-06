'''Dada la fecha de nacimiento de una persona y la fecha actual, determinar un
algoritmo que calcule la edad de la persona. Expresar la solución en pseudocódigo.'''

ano_nacimiento= int(input("ingrese año de nacimiento"))
mes_nacimiento= int(input("ingrese mes de nacimiento"))
dia_nacimiento= int(input("ingrese dia de nacimiento"))
ano_actual= int(input("ingrese año actual"))
mes_actual= int(input("ingrese mes actual"))
dia_actual= int(input("ingrese día actual"))

if mes_actual >= mes_nacimiento:
    if dia_actual >= dia_nacimiento:
        edad = ano_actual - ano_nacimiento
    else:
        edad = ano_actual - ano_nacimiento - 1
else:
    edad = ano_actual - ano_nacimiento - 1

print(edad)