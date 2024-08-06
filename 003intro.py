''' Elaborar un algoritmo que solicite el número de respuestas
correctas, incorrectas y en blanco que ha tenido un estudiante en un examen. Luego
el algoritmo deberá mostrar el puntaje obtenido, siendo que cada respuesta correcta
tendrá 4 puntos, cada respuesta incorrecta tendrá -1 y las respuestas en blanco
valen 0.'''
r_correctas= (int(input("¿Cuántas respuestas correctas tuvo el alumno en el exámen?")))
r_incorrectas= (int(input("¿Cuántas respuestas incorrectas tuvo el alumno en el exámen?")))
print ("El alumno tuvo un puntaje total de ", (r_correctas*4+r_incorrectas*(-1)))