"""Ejercicio 1
Escribir una función que escriba una receta de cocina. Para eso se deben recibir tres listas (la primera
contiene las cantidades de cada ingrediente, la segunda las unidades (ml, g, unidades) y la tercera el
nombre del ingrediente) y una cadena con el procedimiento.
Por ejemplo:
Parámetros: [100,50,1], ["g", "ml", "unidades"], ["Harina", "Leche", "Huevo"] y
"Mezclar todo y cocinar"
Salida:
Ingredientes:
 100 g de Harina
 50 ml de Leche
 1 unidades de Huevo
Procedimiento:
 Mezclar todo y cocinar
Lo que imprime la función debe ser siguiendo el patrón anterior (imprimir "Ingredientes", luego los
ingredientes con una indentación (unos 4 caracteres en blanco) y cuando se muestra un ingrediente se
muestra la cantidad, luego un espacio en blanco, luego la unidad, luego " de " y luego el ingrediente
propiamente dicho.
Si las listas de unidades, cantidades e ingredientes no coinciden debe mostrar un cartel indicando el
inconveniente.
Aclaración: debe funcionar para una receta con cualquier cantidad de ingredientes."""

def receta (l_cantidades, l_unidades, l_ingredientes, procedimiento):
    if len(l_cantidades) != len(l_unidades) and len(l_cantidades)!= len(l_ingredientes) and len(l_unidades) != len(l_ingredientes):
        print("Error de ingresos, las cantidades, unidades, e ingredientes, deben tener las mismas cantidades de elementos")
    else:
        print(f"Ingredientes: \n")
        print(f"    {l_cantidades[0]} {l_unidades[0]} de {l_ingredientes[0]}")
        print(f"    {l_cantidades[1]} {l_unidades[1]} de {l_ingredientes[1]}")
        print(f"    {l_cantidades[2]} {l_unidades[2]} de {l_ingredientes[2]}")
        print(f"\nProcedimiento:\n  \n    {procedimiento}")
    
receta ([100, 50, 1],["g", "ml", "unidades"],["Harina", "Leche", "Huevo"], "Mezclar todo y cocinar")
