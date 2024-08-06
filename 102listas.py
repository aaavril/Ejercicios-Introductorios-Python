"""DESAFÍO 4: PIEZAS DENTALES
Escribir una función que recibe una cadena de caracteres de la forma:
XX,XX,XX,....,XX, donde XX es un número que representa una pieza dental y valide si 
todos los números de piezas de la cadena son números dentales válidos.

Los odontólogos identifican las piezas dentales con un número de dos cifras y se considera 
una pieza dental a los números que estén en los siguientes rangos (inclusive):

Entre 11 y 18

Entre 21 y 28

Entre 31 y 38

Entre 41 y 48

Entre 51 y 55

Entre 61 y 65

Entre 71 y 75

Entre 81 y 85

La función deberá devolver True si todas las piezas dentales de la cadena son números correctos y False en caso contrario. 

Los números presentes en la cadena están separados por comas. Puede pasar que por un error de digitación 
alguien haya ingresado un número de más o menos de dos cifras o algún carácter no válido.
Por ejemplo: 11,24,15,33,27, significa que trabajó en el diente 11, luego en el 24, etc. 
Pero cada número debe estar en uno de los rangos.

"""

def piezas_dentales (cadena):
    lista= cadena.split(", ")
    for i in lista:
        i = int(i)
        if i >= 11 and i <= 18 or i >=21 and i <= 28 or i >= 31 and i <= 38 or i >= 41 and i <= 48  or i >= 51 and i <= 55 or i >= 61 and i <= 65 or i >= 71 and i <= 75 or i >= 81 and i <= 85: 
            valor= True
        else:
            valor= False
            break
    return valor


cadena = "11, 12, 20, 21"
print(piezas_dentales(cadena))  # Devuelve: False

cadena_valida = "11, 12, 21, 22"
print(piezas_dentales(cadena_valida))  # Devuelve: True