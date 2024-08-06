"""3. Implementar una clase para identidades de personas. La clase debe tener los componentes usuales para 
la identificación de las personas como el número de la cédula, una dirección, nombres y apellidos, 
número de teléfono, edad etc. Se debe incluir métodos de acceso a todas las propiedades.

"""

class Persona:
    def __init__(self, apellidos,nombres, cedula, direccion, telefono):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
    def get_nombres(self):
        return self.nombres
    def set_nombres(self, nombres):
        self.nombres = nombres
    def get_apellidos(self):
        return self.apellidos
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    def get_cedula(self):
        return self.cedula
    def set_cedula(self, cedula):
        self.cedula = cedula
    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion
    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono = telefono
    def __str__(self):
        return f"{self.apellidos}, {self.nombres}: CI: {self.cedula}, Direccion:{self.direccion}, {self.telefono}"

# Ejemplos de invocación:
persona1 = Persona("Garcia","Fernando",66983345,"Paraguay 1345","55-55555")
persona2 = Persona("Hernandez","MARIA",66983345,"Pozos del Rey 345","555-55374")
print(persona1)
print(persona2)

# Modificar un atributo
persona2.set_nombres("Maria")
print(persona2)