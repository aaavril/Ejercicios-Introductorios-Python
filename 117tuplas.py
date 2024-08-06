"""Construir una función en Python que reciba por parámetro una lista de nombres de 
personas y devuelva en una tupla la cantidad de nombres que empiezan con 'P', 'M ', 'A'  y 'C'.
"""
def nombres(listaNombres):
  # creo variables para sumar la cantidad de nombres que empiezan con cada letra
  ctdNombresP = 0
  ctdNombresM = 0
  ctdNombresA = 0
  ctdNombresC = 0

  # recorremos los nombres y verificamos la primera letra de cada nombre. Si corresponde a una P, M, A o C sumo 1 a la variable correspondiente
  for nombre in listaNombres:
    if nombre[0] == 'P' or nombre[0] == 'p':
      ctdNombresP += 1
    elif nombre[0] == 'M' or nombre[0] == 'm':
      ctdNombresM += 1
    elif nombre[0] == 'A' or nombre[0] == 'a':
      ctdNombresA += 1
    elif nombre[0] == 'C' or nombre[0] == 'c':
      ctdNombresC += 1


  # devuelvo una tupla con los valores de las variables anteriores
  return (ctdNombresP, ctdNombresM, ctdNombresA, ctdNombresC)

def letras1(lista_nombres):
    #inicializar variables
    lista_resultado= []    
    lista_letras= ["P", "M", "A", "C"]

    #hacer que todos los nombres tengan una letra mayúscula al principio
    for k in range(len(lista_nombres)):
        a = lista_nombres[k]
        a= a.capitalize()
        lista_nombres[k]= a
    
    #recorrer cada letra
    for i in range(len(lista_letras)):
        contador= 0
        letra= lista_letras[i]
        #recorrer cada nombre viendo si la primera letra en cad nombre es igual a la letra
        for j in range(len(lista_nombres)):
            if letra == lista_nombres[j][0]:
                contador += 1
        #retornar el resultado de cada letra y agregarlo a una lista
        resultado= (letra, contador)
        lista_resultado.append(resultado)

    return(lista_resultado)

def letras2(lista_nombres):
    #inicializar variables
    tupla_resultado= ()   
    lista_letras= ["P", "M", "A", "C"]

    #hacer que todos los nombres tengan una letra mayúscula al principio
    for k in range(len(lista_nombres)):
        a = lista_nombres[k]
        a= a.capitalize()
        lista_nombres[k]= a
    
    #recorrer cada letra
    for i in range(len(lista_letras)):
        contador= 0
        letra= lista_letras[i]
        #recorrer cada nombre viendo si la primera letra en cad nombre es igual a la letra
        for j in range(len(lista_nombres)):
            if letra == lista_nombres[j][0]:
                contador += 1
        #retornar el resultado de cada letra y agregarlo a una lista
        resultado= (letra, contador)
        tupla_resultado= tupla_resultado+resultado

    return(tupla_resultado)

lista_nombres=["Paula", "carla", "Josefa", "Avril"]
print(letras1(lista_nombres))
print(letras2(lista_nombres))
print(nombres(lista_nombres))

