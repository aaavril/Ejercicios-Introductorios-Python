"""11. El siguiente código Python permite obtener desde Internet el libro "Cuentos de Amor de Locura y de Muerte de Horacio Quiroga" desde el Proyecto Gutenberg (permite descarga gratuita de e-books):

from urllib.request import urlopen
link = 'https://www.gutenberg.org/cache/epub/13507/pg13507.txt'
f = urlopen(link)
myfile = f.read().decode('utf-8')
print(myfile)


La función read() nos devuelve una cadena de caracteres (string) con el contenido completo del libro.

Crear una función que permita obtener las 5 letra más utilizadas en todo el libro."""


#hacer a todo minuscula y sin caracteres no alfabéticos
#hacerlo una lista
#recorrer la lista y para cada palabra hacer lo mismo que en el ejercicio anterior de que si no esta agregarlo con valor un y si está updatearlo con +1
#cambiarlo a una lista de tupla con items
#usar sort para ordenarlo
#slicear los ultimos 5

from urllib.request import urlopen
def obtener_texto():
    link = 'https://www.gutenberg.org/cache/epub/13507/pg13507.txt'
    f = urlopen(link)
    texto = f.read().decode('utf-8')
    return texto

def frecuencia_letras(texto): 
    letras = {}
    texto= texto.lower()
    for letra in texto:
        if letra.isalpha(): # isalpha() es un método de string que retorna True si el contenido de la variable letra esta compuesto por caracteres del alfabeto.
            letras[letra] = letras.get(letra,0) + 1 #IMPORTANTE ÚTIL
    return letras

texto = obtener_texto()
lista = []
letras = frecuencia_letras(texto)
# Para obtener las 5 letras más utilizadas creamos una lista de sublistas, cada sublista tendra la cantidad de letras en la primera posición y la letra en la segunda posición, de esa forma podemos ordenar la lista en orden descendiente usando un parámetro del sort: reverse=True Hay otras formas mejores de hacerlo, pero esta no implica agregar herramientas no vistas en el curso.
for letra, cantidad in letras.items():
    lista.append([cantidad, letra])
    lista.sort(reverse=True)
for elem in lista[:5]:
    print(elem[1] + ": " + str(elem[0]))
