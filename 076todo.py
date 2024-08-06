"""Implementar en Python una función que recibe un párrafo de un libro (como cadena de caracteres) y
devuelve la cantidad de palabras del párrafo. No se puede utilizar el método split() de Python.
"""
def limpiar_texto(texto):
    texto_limpio = ""
    for caracter in texto:
        if caracter.isalpha() or caracter.isspace():
            texto_limpio += caracter
    return texto_limpio 

def contar_palabras (texto):
    texto= limpiar_texto (texto)
    print (texto)
    contador_palabras= 0
    for i in texto:
        if i == " ":
            contador_palabras += 1
    return contador_palabras+1     



print (contar_palabras("Se pueden especificar diferentes formatos para representar números, como flotantes con un número fijo de dígitos decimales, notación exponencial, formato hexadecimal, formato binario, entre otros."))