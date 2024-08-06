"""2.  Implementar una clase Mascota que describa las mascotas. La clase debe tener las siguientes 
características: especie, nombre, color y veterinaria. Implementar los métodos para acceder a los 
atributos y para imprimir el objeto.

"""
class Mascota:
    def __init__(self, especie, nombre, color, veterinaria):
        self.especie = especie
        self.nombre = nombre
        self.color = color
        self.veterinaria = veterinaria
    def get_especie(self):
        return self.especie
    def set_especie(self, especie):
        self.especie = especie
    def get_nombre(self):
        return self.nombre
    def set_nombre(self):
        self.nombre = self.nombre
    def get_veterinaria(self):
        return self.veterinaria
    def set_veterinaria(self, veterinaria):
        self.veterinaria = veterinaria
    def __str__(self):
        return f"MASCOTA\n\tNombre: {self.nombre}\n\tEspecie: {self.especie}\n\tColor:{self.color}\n\tVeterinaria: {self.veterinaria}"
    
    # Ejemplo de creacion de objetos
mascota1 = Mascota("Perro", "Fido", "beige", "La Mascota")
mascota2 = Mascota("Gato", "Shadow", "negro", "Movil Vet")
mascota3 = Mascota("Gato", "Clarence", "naranja", "Salud Animal")
    
print(mascota1)
print(mascota2)
print(mascota3)

# Ejemplo de modificar un atributo
mascota3.set_veterinaria("La Mascota")
print(mascota3)