"""Desarrollar una función que reciba dos cadenas de caracteres y que retorne 
una cadena con los carácteres
comunes (que aparezcan en una cadena y en la otra), pero sin tener duplicados. 
Si no tienen caracteres
comunes debe retornar una cadena vacía. Considerar que las cadenas pueden tener mayusculas y
minusculas, para este ejercicio un caracter mayusculas y el mismo en minuscula califican como caracteres
comunes, lo mismo para los caracteres acentuados. Ignorar los espacios.
ejercicios-preparacion-parcial2.md 2023-10-16
3 / 6

Ejemplos:
caracteres_comunes("banana", "Anana") # retorna: 'an'
caracteres_comunes("Programar", "picar código") # retorna: ‘proga’
caracteres_comunes("pepe", "juan") # retorna: ''"""

def normalizar_caracteres(texto):
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u', 'Ü': 'u', 'Ñ': 'n'
    }
    texto_normalizado = ""
    for caracter in texto:
        caracter = caracter.lower()
        if caracter in reemplazos:
            texto_normalizado += reemplazos[caracter]
        elif caracter != ' ':
            texto_normalizado += caracter
    return texto_normalizado

def caracteres_comunes (cadena1, cadena2):
    cadena1= normalizar_caracteres(cadena1)
    cadena2= normalizar_caracteres(cadena2)
    nueva_cadena= ""
    for i in cadena1.lower():
        if i in cadena2 and i not in nueva_cadena:
            nueva_cadena= nueva_cadena + i 
    return nueva_cadena      

print (caracteres_comunes ("Holala1234?ú", "olá21  0"))

