"""Objetos """

class Alumno:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, edad):
        self.nombre= nombre
        self.apellido= apellido
        self.cedula= cedula
        self.direccion= direccion
        self.telefono= telefono 
        self.edad= edad
    
    def __str__(self):
        return f"Los datos del alumno son:\nNombre: {self.nombre}\nApellido: {self.apellido}\nCédula de identidad: {self.cedula}\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nEdad:{self.edad}"

    def puede_votar(self):
        return (self.edad>=18)
    
juan_perez= Alumno("Juan", "Perez", "55988554", "Javier de Viana", "096075098", 18 ) 
print(juan_perez)
print(juan_perez.puede_votar())