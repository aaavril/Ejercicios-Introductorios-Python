"""Crear una función que reciba por parámetro una cadena de la forma “hh:mm:ss” donde hh es la hora en
valores de 0 a 23, mm son los minutos en valores de 0 a 59 y ss son los segundos en valores de 0 a 59 y
retorna otra cadena de la forma: “Hora: HH <AM o PM>, Minutos: MM, Segundos: SS” , donde HH es la hora
en valores de 0 a 12, se debe especificar si es AM o PM, MM son los minutos y SS los segundos.
Por ejemplo:
Invocar la función con el parámetro "15:35:10" devuelve: "Hora: 3 PM, Minutos: 35,
Segundos: 10"
Invocar la funcion con el parámetro "08:05:00" devuelve: "Hora: 8 AM, Minutos: 5,
Segundos: 0"""

def transformar_horario (hora):
    hh= hora[:2]
    mm= hora[3:5]
    ss= hora[6:]
    hh=int(hh)
    if hh>=12:
        if hh>12:
            hh=hh-12
        return (f"Hora: {hh} PM, Minutos: {mm}, Segundos: {ss}")
    else:
        return (f"Hora: {hh} AM, Minutos: {mm}, Segundos: {ss}")

print(transformar_horario("12:05:00"))

