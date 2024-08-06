"""2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de una carrera 
{'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación: 6, 'Redacción': 6, 'Trabajo final': 6}. 
Luego debe mostrar por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas de la carrera, y <créditos> son sus créditos. Al final debe mostrar 
también el número total de créditos.
"""

diccionario_creditos= {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación':6, 'Redacción': 6, 'Trabajo final': 6}
contador= 0

for i in diccionario_creditos:
    print(f"{i} tiene {diccionario_creditos[i]} créditos")
    contador += diccionario_creditos[i]

print(f"El total de créditos es {contador}")