"""4.  Implementar una clase modelando una cuenta bancaria. La cuenta bancaria tiene un saldo, 
un número de cuenta, e información sobre el dueño, que es una instancia de la clase anterior 
(ejercicio 3). La clase debe implementar los métodos de hacer un depósito o una extracción de dinero. 
El método de extracción de dinero debe rechazar la transacción si no hay fondos suficientes en la cuenta. 
También desarrollar una función transferencia que mueve un monto entre una y otra cuenta (Para esto se puede 
realizar una extracción seguido por un depósito). Esos métodos y funciones deben devolver un valor lógico 
indicando si se fue posible ejecutar la transacción.

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
    
class Cuenta:
    def __init__(self, numero_cuenta, persona, saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.persona = persona
        self.saldo = saldo_inicial
    def get_numero_cuenta(self):
        return self.numero_cuenta
    def get_persona(self):
        return self.persona
    def set_persona(self, persona):
        self.persona = persona
    def extraer(self, monto):
        if monto > self.saldo:
            return False # Indica que no se pudo realizar la operacion por falta de fondos
        else:
            self.saldo = self.saldo - monto
            return True # Indica que la operación se pudo realizar
    def deposito(self, monto):
        self.saldo = self.saldo + monto
    def transferir(self, otra_cuenta, monto):
        if self.extraer(monto):
            otra_cuenta.deposito(monto)
            return True # se pudo realizar la operación
        else:
            return False # No se pudo realizar la operación
    def __str__(self):
        return f"Numero de cuenta: {self.numero_cuenta}\nPersona: {self.persona}\nSaldo: {self.saldo}"

persona1 = Persona("Garcia","Fernando",65498332,"","")
persona2 = Persona("Hernandez","Maria",55678433,"","")
cuenta1 = Cuenta(1, persona1, 100.0)
cuenta2 = Cuenta(2, persona1, 0.0)
cuenta3 = Cuenta(3, persona2, 1800.0)
cuenta4 = Cuenta(4, Persona("Vaz","Pedro",2345671,"",""), 3500.0)# Podemos crear la cuenta sin crear una Persona en una variable

print(cuenta1)
print(cuenta2)
print(cuenta3)
print(cuenta4)
print()
print("Extracción de 150 pesos de la cuenta 0001")
print(cuenta1)

if cuenta1.extraer(150):
    print("Operación exitosa, se actualizo el saldo")
    print(cuenta1)
else:
    print("No se pudo realizar la operación, por falta de fondos.")
    print()
    print("Extracción de 150 pesos de la cuenta 0003")
    print(cuenta3)

if cuenta3.extraer(150):
    print("Operación exitosa, se actualizo el saldo")
    print(cuenta3)
else:
    print("No se pudo realizar la operación, por falta de fondos.")
    print()
    print("Transferir 1300 de la cuanta 0004 a la cuenta 0002")
    print(cuenta4)
    print(cuenta2)

if cuenta4.transferir(cuenta2, 1300.00): # se transfier de cuenta 0004 a la cuenta 0002
    print("Operacion exitosa, se actualizaron los saldos")
    print(cuenta4)
    print(cuenta2)
else:
    print("No se pudo realizar la operacion por falta de fondos.")
    print()
