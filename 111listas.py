"""escribir una función que escriba una receta de cocina. Para eso se edben escribir tres listas 
(la primera contiene la cantidad fr ingredientes, la segunda la cantidad de cada ingrediente, la segunda las unidades 
(ml, g, unidades), y la tercera el nombre de ingrediente, y una cadena con el procedimiento.))"""

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
