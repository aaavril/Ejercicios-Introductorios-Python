"""Ejercicio 2

Escribe un programa que simule un sistema de gestión de tarjetas de crédito. Utiliza la clase 
TarjetaDeCredito proporcionada y sigue las instrucciones a continuación.

Crea un diccionario llamado tarjetas para almacenar las tarjetas de crédito. Inicialmente, 
el diccionario estará vacío.

Implementa un menú con las siguientes opciones: 

a. "Crear tarjeta": Solicita al usuario 
ingresar los datos necesarios para crear una tarjeta de crédito, incluyendo el número de cédula, 
número de tarjeta, titular, fecha de vencimiento, CVV y límite de crédito. Utiliza estos datos para 
crear una instancia de la clase TarjetaDeCredito y agrégala al diccionario tarjetas con el número 
de cédula como clave. 

b. "Realizar pago": Solicita al usuario ingresar el número de cédula 
correspondiente a la tarjeta de crédito en la que desea realizar un pago. Luego, solicita 
el monto del pago y el motivo. Utiliza el método realizar_pago de la clase TarjetaDeCredito 
para realizar el pago en la tarjeta correspondiente. 

c. "Consultar saldo": Solicita al usuario 
ingresar el número de cédula correspondiente a la tarjeta de crédito de la cual desea consultar
 el saldo. Utiliza el método saldo de la clase TarjetaDeCredito para obtener el saldo actual de la tarjeta 
 y muestra el resultado por pantalla. 
 
 d. "4. Imprimir información de tarjeta": Solicita al usuario 
 ingresar el número de cédula correspondiente a la tarjeta de crédito de la cual desea imprimir la información. 
 Utiliza el número de cédula como clave para acceder a la tarjeta en el diccionario tarjetas y muestra la información" 
 
 e. 
 "Salir": Finaliza el programa.

Implementa un bucle que solicite al usuario elegir una opción del menú y ejecute 
la operación correspondiente hasta que el usuario elija la opción de salir.

"""
class TarjetaDeCredito:
    def __init__(self, numero, titular, fecha_vencimiento, cvv, limite_credito):
        self.numero = numero
        self.titular = titular
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv
        self.limite_credito = limite_credito
        self.historico_pagos = []

    def realizar_pago(self, monto, motivo):
        if self.saldo() + monto <= self.limite_credito:
            pago = {"monto": monto, "motivo": motivo}
            self.historico_pagos.append(pago)
            print(f"Se realizó un pago de ${monto} con la tarjeta {self.numero} - Motivo: {motivo}")
        else:
            print("No se puede realizar el pago. Límite de crédito excedido.")

    def saldo(self):
        total_pagos = sum(pago["monto"] for pago in self.historico_pagos)
        return total_pagos

    def obtener_numero(self):
        return self.numero

    def obtener_titular(self):
        return self.titular

    def obtener_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def obtener_cvv(self):
        return self.cvv

    def obtener_limite_credito(self):
        return self.limite_credito

    def obtener_historico_pagos(self):
        if not self.historico_pagos:
            return "No se han registrado pagos."

        historico_tabla = f"{'Monto':<10} {'Motivo':<20}\n"
        historico_tabla += "-" * 30 + "\n"

        for pago in self.historico_pagos:
            monto = pago["monto"]
            motivo = pago["motivo"]
            historico_tabla += f"${monto:<10} {motivo:<20}\n"

        return historico_tabla

    def __str__(self):
        estado = f"Tarjeta de Crédito\n"
        estado += f"Número: {self.numero}\n"
        estado += f"Titular: {self.titular}\n"
        estado += f"Fecha de Vencimiento: {self.fecha_vencimiento}\n"
        estado += f"CVV: {self.cvv}\n"
        estado += f"Límite de Crédito: ${self.limite_credito}\n"
        estado += f"Saldo Actual: ${self.saldo()}\n"
        estado += f"\nHistorial de Pagos:\n{self.obtener_historico_pagos()}"
        return estado

diccionario_tarjetas= {}
bandera= True

while bandera:
    opción= input("a. Crear tarjeta\nb. Realizar pago\nc. Consultar saldo\nd. Imprimir información de tarjeta\ne. Finalizar el programa\nOpción: ")
    
    if opción== "e": #funcioan
        bandera= False 
    
    elif opción== "a": #funciona
        numero= input("Ingrese número de tarjeta: ") 
        titular= input("Ingrese Nombre de titular: ")
        fecha_vencimiento= input("Ingrese fecha de vencimiento: ")
        cvv= input("Ingrese número CVV: ")
        limite_credito= int(input("Ingrese límite de crédito: "))
        titular= TarjetaDeCredito(numero, titular, fecha_vencimiento, cvv, 2000)
        diccionario_tarjetas.update({numero: titular})
    
    elif opción== "b": #no funciona
        numero= (input("Ingrese número correspondiente a la tarjeta: "))
        monto= int(input("Ingrese el monto de pago: "))
        motivo= input("Ingrese el motivo del pago: ")
        diccionario_tarjetas[numero].realizar_pago(monto, motivo)
    
    elif opción== "c": #funciona
        numero= (input("Ingrese número correspondiente a la tarjeta: "))
        print(diccionario_tarjetas[numero].saldo())
    
    elif opción== "d": #funciona
        numero= (input("Ingrese número correspondiente a la tarjeta: "))
        print(diccionario_tarjetas[numero])
    
    else: #funciona
        print("opción no válida")

print(diccionario_tarjetas)
        