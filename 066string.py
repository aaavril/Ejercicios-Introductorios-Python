'''Las palabras mágicas son aquellas que su valor gemátrico es 21. 
Crear una función que devuelva True si una palabra es mágica y False en caso contrario.
'''
def valor_gematrico (texto):
    abecedario= "abcdefghijklmnñopqrstuvwxyz"
    suma= 0
    for i in texto.lower():
        if i in abecedario:
            pos= abecedario.find(i)
            suma= suma+pos+1
    return suma==21        

print (valor_gematrico("alga"))

