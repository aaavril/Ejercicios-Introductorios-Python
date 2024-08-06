'''Crear una función “pangrama” que recibe una cadena de caracteres e indica 
si la misma es un pangrama. Un pangrama es una cadena de caracteres que 
contiene todas las letras posibles de alfabeto ya sea en mayúsculas o 
minúsculas (español para nuestro caso).

Ej: El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón.'''

def pangrama (texto):
    abecedario= "abcdefghijklmnñopqrstuvwxyz"
    letras = ""
    for i in texto.lower():
        if i in abecedario and i not in letras:
            letras= letras+i
    return len(letras)== len(abecedario)

print (pangrama ("abcdefghijklmnñopqrstuvwxyz"))         