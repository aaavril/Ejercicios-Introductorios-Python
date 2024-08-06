'''Dada una hora (horas, minutos y segundos), desarrollar una función que devuelva la 
hora en un string en formato hh:mm:ss (note que podemos convertir números a strings 
usando la función str y podemos concatenar strings usando el operador "+").
'''

def horario(horas, minutos, segundos):
    shoras, sminutos, ssegundos = horas, minutos, segundos
    if horas < 10:
        shoras = "0" + str(horas)
    else:
        shoras = str(horas)
        
    if minutos < 10:
        sminutos = "0" + str(minutos)
    else:
        sminutos = str(minutos)
        
    if segundos < 10:
        ssegundos = "0" + str(segundos)
    else:
        ssegundos = str(segundos)
        
    horario_formateado = f"{shoras}:{sminutos}:{ssegundos}"
    return horario_formateado

print(horario(8, 40, 17))