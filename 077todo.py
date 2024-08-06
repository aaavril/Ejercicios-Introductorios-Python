"""Sea una cadena de caracteres c. Decimos que una vocal v dentro de c está en equilibrio si la cantidad de
vocales a la izquierda de v es igual a la cantidad de vocales a la derecha (podrían ser cero vocales).
Implementar una función en Python que dado un string retorne la ubicación en donde se encuentra la vocal
en equilibro (si es que la hay); si no tiene vocal en equilibrio debe retornar -1 (los strings con un número par
de vocales no tiene vocal en equilibrio). Es claro que una cadena tiene una sola vocal en equilibrio o
ninguna.
La función debe definirse con el nombre en_equilibrio(c). Tenga en cuenta que se considerarán como
vocales incluso las vocales mayúsculas y minúsculas, y las acentuadas.
Ejemplos:
"Programación" está en equilibrio (la vocal en equilibrio es la segunda "a", pues tiene 2 vocales
antes y dos vocales después), por lo tanto la función debería devolver 7 (que es la posición dentro del
string de la vocal en equilibrio)
"perro" no tiene vocal en equilibrio, por lo tanto retornará -1
"pez" tiene a la "e" en quilibrio porque no hay ninguna tanto a izquierda como a derecha, por lo tanto
retornará 1 (posición de la vocal "e"
"Ágora" está en equilibrio (notar de que se debe contemplar a las vocales acentuadas y mayúsculas).
Defina una función es_vocal(letra) que retorne True si letra es una de las vocales consideradas
(minúscula, mayúscula, o combinación con acento). Considere además hacer una función que cuente la
cantidad de vocales que tiene un string.
"""

def es_vocal(letra):
    vocales="aeiouáéíóúAEIOUÁÉÍÓÚ"
    return letra in vocales

def cantidad_vocales(cadena):
    contador = 0
    for letra in cadena:
        if es_vocal(letra):
            contador = contador + 1
    return contador

def en_equilibrio(cadena):
    vocales = cantidad_vocales(cadena)
    if vocales % 2 == 0 or vocales == 0: # es par, no hay vocales en equilibrio
        return -1
    else:
        vocal_del_medio = vocales // 2 + 1 # hay que buscar la n vocal
        vocales_encontradas = 1 # empieza con la primera vocal
        posicion = 0 # posición de la vocal en la cadena
        for i in range(len(cadena)):
            if es_vocal(cadena[i]):
                if vocales_encontradas == vocal_del_medio:
                    posicion = i
                    vocales_encontradas = vocales_encontradas + 1
    return posicion

print(en_equilibrio("stxacavb")) # -1
print(en_equilibrio("Programación")) # 7
print(en_equilibrio("perro")) # -1
print(en_equilibrio("pez")) # 1
print(en_equilibrio("Ágora")) # 2