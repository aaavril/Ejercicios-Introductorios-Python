"""Hacer una función en Python que permita ingresar los valores del número diario de infectados por 
Covid-19 hasta que se digite -1 y devuelva en una tupla, el total de valores ingresados, el promedio, 
el valor máximo y el mínimo .

"""
def covid ():
    n= 0
    valores= []
    #ingresar valores y guardarlos en una lista
    while n != -1:
        n= int(input("Ingrese infectados por covid (-1 para terminar el programa): "))
        if n != -1:
            valores.append(n)
    
    #hacer cálculos correspondientes
    minimo= min(valores)
    maximo= max(valores)
    total= sum(valores)
    promedio= total/len(valores)

    #retornar una tupla con todos los valores
    return total, promedio, maximo, minimo


def infectadosCovid():
  numInfectados = 0
  listaValores = []
  # mientras el numero de infectados sea distinto a -1 agrego a una lista los valores
  while(numInfectados != -1):
    numInfectados = int(input("Ingrese el número de infectados de hoy: "))
    if(numInfectados != -1):
      listaValores.append(numInfectados)

  # luego de tener la lista calculo lo que necesito y devuelvo como tupla
  largoLista = len(listaValores)
  sumaLista = sum(listaValores)

  if(largoLista > 0):
    return (largoLista, sumaLista / largoLista, max(listaValores), min(listaValores))
  else:
    return "No ha ingresado valores"

#imprimir función solución 
print(infectadosCovid())
#llamar a la función y desmpaquetar la tupla retornada
total, promedio, maximo, minimo= covid()
#imprimir el resultado fancy
print(f"El total fue {total}, el promedio {promedio}, el máximo {maximo}, y el mínimo {minimo}")
#imprimir el resultado en tupla
print(covid())
