"""Ejercicio 6:
Combinaciones de Palabras
Descripción del problema:
Escribe una función llamada combinaciones_palabras que tome dos listas de palabras como
entrada y genere todas las posibles combinaciones de palabras entre las dos listas. La función
debe devolver una lista de todas las combinaciones posibles, donde cada combinación es una
cadena de palabras separadas por un espacio.
Ejemplo de entrada y salida:
lista1 = ['Hola', 'Adiós']
lista2 = ['mundo', 'amigos']
combinaciones_palabras(lista1, lista2)
Salida:
['Hola mundo', 'Hola amigos', 'Adiós mundo', 'Adiós amigos']"""

def combinaciones_palabras (lista1, lista2):
    combinacion= []
    for i in lista1:
        for j in lista2:
            cadena= i +' '+ j
            combinacion.append(cadena)
    return combinacion

lista1 = ['Hola', 'Adiós']
lista2 = ['mundo', 'amigos']
print(combinaciones_palabras(lista1, lista2))