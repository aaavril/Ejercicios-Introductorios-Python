"""Ejercicio 2
Como sabemos, la cantidad de casos y muertes diarios producidos por la covid19 suele ser bastante
oscilante de un día a otro y para seguir la tendencia de los cambios es mejor obtener la media de últimos n
días. El siguiente gráfico muestra un ejemplo de los últimos 30 días de casos positivos (las barras indican los
casos diarios, la línea llena indica el promedio obtenido de los últimos 7 días)
{
width:50%}
Supongamos que disponemos de una lista, donde cada elemento de la lista es un diccionario. Ese
diccionario tiene dos pares clave valor (dos elementos), uno es "casos":nro de casos y otro que es
"muertos":nro de muertos.
Por ejemplo la lista puede ser la siguiente:
lista=[ { "casos": 3452, "muertos":45},
 { "casos":2269, "muertos":53},
 { "casos":2318, "muertos":54},
 { "casos": 1278, "muertos":33} ,
 { "casos": 2385, "muertos":41},
 { "casos":1185, "muertos":31} ]
(obviamente esa lista tiene muy pocos días)
1. Realice una función que dada una lista con el formato anterior, retorne el promedio de muertos
2. Realice una función que reciba una lista con el formato anterior y un número n y genere una lista con
el promedio móvil de n días. Por ejemplo, si se llamara con la lista anterior y n fuera 3, entonces
debería devolver la lista [(3452+2269+2318)/3, (2269+2318+1278)/3,
(2318+1278+2385)/3, …. ]. Tenga en cuenta que se necesitan n días para calcular el promedio.
OBS: para probar el código puedes usar la lista ejemplo"""

def promedio_muertes(lista_diccionarios):
    contador_muertes= 0
    contador_dias= 0
    for dias in lista_diccionarios:
        muertes= dias["muertos"]
        contador_muertes+= muertes
        contador_dias+= 1
    promedio= contador_muertes/contador_dias
    return promedio

def promedio_movil_casos(lista_diccionarios, n):
    lista_promedios= []
    for dias in range(len(lista_diccionarios)-n+1):
        contador_casos_n= 0
        for i in range(n):
            casos= lista_diccionarios[dias+i]["casos"]
            contador_casos_n+=casos
        promedio= contador_casos_n/n
        lista_promedios.append(promedio)
    return lista_promedios

lista=[ { "casos": 3452, "muertos":45},
 { "casos":2269, "muertos":53},
 { "casos":2318, "muertos":54},
 { "casos": 1278, "muertos":33} ,
 { "casos": 2385, "muertos":41},
 { "casos":1185, "muertos":31} ]

print(promedio_muertes(lista))
print(promedio_movil_casos(lista, 3))
print(promedio_movil_casos(lista, 6))
print(promedio_movil_casos(lista, 2))






