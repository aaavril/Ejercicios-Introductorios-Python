"""1. Implementar una clase Bicicleta que describa las bicicletas. La clase debe tener las siguientes 
características de una bici: marca, color, tamaño y si es de montaña o ciudad. Implementar los 
métodos para acceder a los atributos y para imprimir el objeto.

"""

class Bicicleta: 
    def __init__(self, marca, color, tamano, tipo): 
        self.marca = marca 
        self.color = color
        self.tamano = tamano
        self.tipo = tipo 
        print(f"Tengo una nueva bici marca {self.marca}\n")

    def __str__(self): 
        return f"*Datos de la bicicleta*\nMarca: {self.marca}\nColor: {self.color}\nTamaño: Rodado {self.tamano}\nTipo(montaña o ciudad): {self.tipo}\n"

    def get_marca(self): 
        return self.marca

    def get_color(self):
        return self.color

    def get_tamano(self):
        return self.tamano

    def get_tipo(self):
        return self.tipo

bici_caro= Bicicleta("Treck", "Dorada", "24", "Montaña")
print(bici_caro)
print(bici_caro.get_marca())
print(bici_caro.get_color())
print(bici_caro.get_tamano())

"""Opción de la soluciómn profes que tienen funciones set"""

# class Bicicleta:
#     def __init__(self,marca, color, tamaño, tipo):
#         self.marca = marca
#         self.color = color
#         self.tamaño = tamaño
#         self.tipo = tipo
#     def get_marca(self):
#         return self.marca
#     def set_marca(self, marca):
#         self.marca = marca
#     def get_color(self):
#         return self.color
#     def set_color(self, color):
#         self.color = color
#     def get_tamaño(self):
#         return self.tamaño
#     def set_tamaño(self, tamaño):
#         self.tamaño = tamaño
#     def __str__(self):
#         return f"BICICLETA\n\tMarca: {self.marca},\n\tColor: {self.color},\n\tTamaño:{self.tamaño},\n\tTipo: {self.tipo}\n"

# # Ejemplos de creación de objetos:
# bici1 = Bicicleta("Graciela","celeste","Rodado 20","Ciudad")
# bici2 = Bicicleta("Trek","negra","Rodado 24","Ciudad")
# bici3 = Bicicleta("Mountan Bike","azul","Rodado 26","Montaña")

# print(bici1)
# print(bici2)
# print(bici3)

# bici1.set_color("azul")

# print(bici1.get_color())
