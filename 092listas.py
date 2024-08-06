
"""3. Escribir una función que tome una lista de cadenas de caracteres y 
una cadena adicional como parámetro y devuelva True si la cadena está en lista o False sino."""

def cadena_in_lista (lista, cadena):
    existe= False 
    for i in lista:
        if i== cadena:
            existe = True
    return existe

print (cadena_in_lista (["Hola", "como", 1, 2], "Hola") )
print (cadena_in_lista (["Hola", "como", 1, 2], "uno") )
