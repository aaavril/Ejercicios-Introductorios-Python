"""1. Crear una función vocales(palabra) que dada una palabra (una cadena de caracteres), devuelva la
cantidad de vocales que tiene (deben considerarse todas las variantes mayúsculas, minúsculas y las
que llevan tildes).
Ej: vocales("María") # retorna: 3
2. Utilizando (invocando) la función anterior, crear una función que dada una palabra (una cadena de
caracteres), devuelva la cantidad de consonantes que tiene.
Ej: consonantes(“María”) # retorna: 2
NOTA: La palabra no contiene ni espacios ni símbolos.
"""

def vocales(palabra):
    cadena_vocales = "aeiouáéíóú"
    contador = 0
    for letra in palabra.lower():
        if letra in cadena_vocales:
            contador = contador +1
    return contador

def consonantes(palabra):
     return len(palabra) - vocales(palabra)

print('vocales("María")','->',vocales("María"))
print('vocales("MarÌa")','->',vocales("MarÍa"))
print('consonates("María")','->',consonantes("María"))