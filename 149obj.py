"""Ejercicio 1

Escribir un programa que simule el uso de tarjetas de crédito. Se te proporciona la 
clase TarjetaDeCredito con los métodos y atributos necesarios. Tu tarea es crear 
al menos dos instancias de la clase TarjetaDeCredito con los siguientes datos:

Tarjeta 1:

Número: "1234567890123456"
Titular: "Adela Sanchez"
Fecha de vencimiento: "12/26"
CVV: "123"
Límite de crédito: $2000

Tarjeta 2:

Número: "9876543210987654"
Titular: "Juan Oreste"
Fecha de vencimiento: "06/25"
CVV: "456"
Límite de crédito: $1500
A continuación, realiza las siguientes operaciones utilizando los métodos de la clase TarjetaDeCredito:

Para cada tarjeta, realiza un pago de $500 con el motivo "Compra en línea".
Para cada tarjeta, realiza un pago de $1000 con el motivo "Pago de factura".
Para cada tarjeta, realiza un pago de $250 con el motivo "Nafta".
Para la tarjeta 1 agrega un pago de 50$ con el motivo "Regalos".
Finalmente, muestra por pantalla el estado actual de cada tarjeta. Para esto investiga el método __str__. Verifica que este método está implementado.

Recuerda utilizar los métodos de la clase TarjetaDeCredito para realizar las operaciones y obtener la información necesaria:

   Métodos disponibles:

    - realizar_pago(monto, motivo): Realiza un pago con la tarjeta de crédito.
    - saldo(): Retorna el saldo actual de la tarjeta.
    - obtener_numero(): Retorna el número de la tarjeta.
    - obtener_titular(): Retorna el nombre del titular de la tarjeta.
    - obtener_fecha_vencimiento(): Retorna la fecha de vencimiento de la tarjeta.
    - obtener_cvv(): Retorna el código de seguridad de la tarjeta.
    - obtener_limite_credito(): Retorna el límite de crédito de la tarjeta.
    - obtener_historico_pagos(): Retorna el historial de pagos realizado en forma tabulada.
    - __str__(): Retorna una representación en forma de cadena del estado actual de la tarjeta.

    Ejemplo de uso:
    # Crear una instancia de TarjetaDeCredito
    tarjeta = TarjetaDeCredito("1234567890123456", "John Doe", "12/24", "123", 2000.0)"""

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


titular_1= TarjetaDeCredito("1234567890123456", "Adela Sanchez", "12/26", "123", 2000)
titular_2= TarjetaDeCredito("9876543210987654", "Juan Oreste", "06/25", "456", 1500)

print(titular_1)
print(titular_2)

titular_1.realizar_pago(500, "Compra en línea")
titular_1.realizar_pago(1000, "Pago de factura")
titular_1.realizar_pago(250, "Nafta")
titular_1.realizar_pago(50, "Regalo")
titular_2.realizar_pago(500, "Compra en línea")
titular_2.realizar_pago(1000, "Pago de factura")
titular_2.realizar_pago(250, "Nafta")

print(titular_1)
print(titular_2)

