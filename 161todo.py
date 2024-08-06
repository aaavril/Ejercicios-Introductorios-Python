"""función historgrama: toma cadena caracteres como parametro y devuelve un diccionario dónde 
cada carácter de la cadena es una clase y tiene asociada la cantidad de veces que aparece en la cadena. 
Se debe tener en cuenta mayúsculas y minúsculas. No contiene carácteres acentuados ni símbolos de puntuación"""


def histograma(cadena): 
    histograma = {}
    cadena= cadena.upper() 
    for letra in cadena:
        histograma[letra] = histograma.get(letra,0) + 1 #IMPORTANTE ÚTIL
    return histograma

def estadisica(histograma):
    lista_llaves= histograma.keys()

    #calcular vocales y consonantes
    cantidad_vocales= 0
    cantidad_consonantes= 0
    cantidad_espacios= histograma[" "]

    for i in lista_llaves:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            cantidad_vocales+= histograma[i]
        elif i == " ":
            cantidad_espacios+= histograma[i]
        else:
            cantidad_consonantes+= histograma[i]

    resultado= [cantidad_vocales, cantidad_consonantes, cantidad_espacios]

    return resultado

histograma= histograma("AEIOU aeiou Hola como estas")
print(histograma)
print(estadisica(histograma))

