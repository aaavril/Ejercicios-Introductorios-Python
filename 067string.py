'''Implementar una función que permite determinar si una palabra es un palíndromo. 
Los palíndromos son aquellas palabras que se leen igual de izquierda a derecha que de 
derecha a izquierda, por ejemplo:

es_palindromo("reconocer") --> True
'''
def capicua (texto):
    espejo= ""
    texto= texto.lower()
    for i in texto [::-1]:
        espejo += i
    return texto==espejo