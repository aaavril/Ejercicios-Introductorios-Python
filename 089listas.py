
def contador_valor (lista, valor): #función que hace lo mismo que count
    total=0
    for i in lista:
        if i == valor:
            total += 1
    return total

def contador (lista): #función que hace lo mismo que len, el for en este caso no le importa el indice 
    total=0
    for i in lista:
        total += 1
    return total

def posicion (lista, valor): #función que hace lo mismo que index, en eset caso como lo importa el indice, el i toma el valor de cada indice y dentro de la función se busca si en ese indice, la función tiene un valor específico
    for i in range(len(lista)):
        if lista[i] == valor:
            return i

def equivalente_in (lista, valor): #función que hace lo mismo que in
    valor_existe= False 
    for i in lista:
        if i == valor:
            valor_existe= True
    return valor_existe 

lista1= ["e", "5", "f", "e", "g", "e"]   
print (contador_valor(lista1, "e"))      
print (lista1.count("e"))

lista2 = ["e","l","e","f","a","n","t","e"]
print (contador(lista2))      
print (len(lista2))

lista3= ["e", "5", "f", "e", "g", "e"]   
print (posicion(lista3, "5"))      
print (lista3.index("5"))

lista4 = ["e","l","e","f","a","n","t","e"]
print (equivalente_in(lista4, "l"))     
print ("l" in lista4)
print (equivalente_in(lista4, "x"))   
print ("x" in lista4)

