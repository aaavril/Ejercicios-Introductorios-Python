'''Crear una función “lipograma” que recibe una cadena de caracteres e 
indica si la misma es un lipograma. Un lipograma es una cadena de 
caracteres que contiene todas las letras posibles de alfabeto 
(español para nuestro caso excepto una. Por ejemplo un texto donde 
nunca aparece la letra “a” pero si aparecen el resto de las letras.'''

def lipograma (c):
    abecedario= "abcdefghijklmnñopqrstuvwxyz"
    letras_unicas = ""
    for i in c.lower():
        if i in abecedario and i not in letras_unicas:
            letras_unicas= letras_unicas+i
    return len(letras_unicas)== len(abecedario)-1

print (lipograma ("abcdefghijklmnñopqrstuvwxyz"))        