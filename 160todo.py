"""escribir función que recibe 3 listas conteniendo palabras. 
La función debe devolver la lista que tiene más letras (la que la 
suma total de letras de palabras de la lista es mayor)"""


def largo_lista (lista):
    cadena= " ".join(lista)
    nueva_cadena= ""
    for i in cadena:
        if i.isalpha():
            nueva_cadena = nueva_cadena+i
    largo_cadena= len(nueva_cadena)
    return largo_cadena

def lista_mayor (lista1, lista2, lista3):
    largo1= largo_lista(lista1)
    largo2= largo_lista(lista2)
    largo3= largo_lista(lista3)
    if largo1>largo2 and largo1>largo3:
        return lista1
    elif largo2>largo3 and largo2>largo1:
        return lista2
    else:
        return lista3

print(lista_mayor(["esto", "tiene", "letras"], ["esto", "también", "tiene", "letras"], ["esto", "tiene", "letras", "también", "más"]))

