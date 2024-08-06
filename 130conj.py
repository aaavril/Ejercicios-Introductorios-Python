"""Volvamos al ejercicio de las revistas, pero esta vez lo resolveremos en python utilizando sets. 
Una encuesta sobre la lectura de 3 revistas A, B y C, sea han obtenido los siguientes datos: de 
10 personas, 6 leen la revista A, 5 la B, 5 la C, 2 la revistas B y C, 3 la C y A, 3 la A y B y 1 las tres.
"""

a={"juan","pepe","maria","jose","esteban","lucia"}
b={"juan","pepe","marta","lucia","john"}
c={"lucia","john","maria","esteban","margarita"}

total_personas = 10
caso_a = (a & b - (a & b & c)) | (b & c - (a & b & c)) | (a & c - (a & b & c))
print("a) ¿cuantos leen 2 y sólo 2 revistas?: ",len(caso_a))

lectores = a | b | c # conjunto de todos los lectores de revista
caso_b = total_personas - len(lectores)
print("b) ¿cuántos no leen ninguna revista?: ",caso_b)

solo_a = a.difference(b.union(c)) #
solo_b = b - (a | c)
solo_c = c - (a | b)
caso_c = solo_a | solo_b | solo_c

print("c) ¿Cuántos leen 1 y sólo 1 revista?: ",len(caso_c))

caso_d = a & b & c
print("d) ¿Qué número de lectores tienen las 3 revistas?: ", len(caso_d))
