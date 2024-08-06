"""Escribir una función genera_contraseña que permite generar contraseñas (por ejemplo para usar como
pin de la cédula digital o para un cajero) cuyos caracteres son únicamente números. Específicamente, la
función recibirá como parámetro la cantidad total n de caracteres que debe tener la contraseña y devolverá
un string con la contraseña generada (naturalmente la contraseña serán n dígitos numéricos generados al
azar).
Por ejemplo, si quiero generar contraseñas de longitud 8:
genera_contraseña(8) -> "56737864"
genera_contraseña(8) -> "09274100""""

from random import randint 

def genera_contraseña(n):
    contra= ""
    for i in range (n):
        contra += str(randint(0,9))
    return contra    

print(genera_contraseña(8))
print(genera_contraseña(8))
print(genera_contraseña(8))
print(genera_contraseña(8))