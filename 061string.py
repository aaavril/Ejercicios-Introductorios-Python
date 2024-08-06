'''Escribir una función que reciba una cadena de caracteres y retorne una 
nueva cadena con los caracteres espacio (“ “) reemplazados por el carácter “;”.'''

def espacios (string):
    s_m= ""
    for i in string:
        if i == " ":
            s_m= s_m+ ";"
        else: 
            s_m= s_m + i
    return s_m        

print(espacios("tengo ojos celestes y amarillos"))

        