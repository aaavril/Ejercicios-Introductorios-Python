''' Gematría es un sistema de origen asiro-babilonio que asigna 
a cada palabra o frase un valor numérico calculado sobre las 
letras en la palabra. El sistema más sencillo suma las letras en 
la frase dando un valor de 1 a cada “a", 2 a cada “b", 3 a cada “c”, etc. 
Los espacios en blanco y símbolos de puntuación se ignoran.

Escribir una función que toma una cadena como argumento y devuelve el valor gemátrico de la cadena.

Ej: valor_gematrico(“aaa bbb”) → 9
'''

def valor_gematrico (texto):
    abecedario= "abcdefghijklmnñopqrstuvwxyz"
    suma= 0
    for i in texto.lower():
        if i in abecedario:
            pos= abecedario.find(i)
            suma= suma+pos+1
    return suma

print (valor_gematrico("hola mundo"))