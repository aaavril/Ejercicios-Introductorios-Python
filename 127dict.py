"""9. Escribir una función que sanitiza una cadena. El método de sanitización es el siguiente:
a. Todas las letras con tilde se cambian por la misma letra sin tilde.

b. Símbolos de pregunta y de exclamación se reemplazan por guiones (“-“)

c. Los espacios se reemplazan por guiones bajos (“_")

d. La "ñ" se reemplaza por la “n"

e. Cualquier otro símbolo (que no sean letras) se remueve."""

def sanitiza_cadena (cadena):
    diccionario= {"¿": "-", "?": "-", "¡": "-", "!": "-", " ": "_", "ñ": "n", "Ñ": "N"}
    nueva_cadena= ""
    for i in range(len(cadena)):
        if cadena[i] in diccionario:
            caracter= diccionario[cadena[i]]
        elif cadena[i].isalpha():
            caracter= cadena[i]
        else:
            caracter= ""
        nueva_cadena += caracter
    return nueva_cadena
    
print(sanitiza_cadena("Hola, jasjasjasj, Ñ"))