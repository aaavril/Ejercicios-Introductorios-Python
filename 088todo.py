
def explicar_decimal_a_binario(decimal):
    pasos = []
    binario = ""
    if decimal == 0:
        return "0", ["El número decimal es 0, por lo tanto el binario también es 0."]
    
    original = decimal
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        pasos.append(f"{decimal} dividido por 2 da un cociente de {decimal // 2} y un residuo de {residuo}.")
        decimal = decimal // 2
    pasos.append(f"El número binario es {binario}.")
    return binario, pasos

def explicar_decimal_a_hexadecimal(decimal):
    pasos = []
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    if decimal == 0:
        return "0", ["El número decimal es 0, por lo tanto el hexadecimal también es 0."]
    
    original = decimal
    while decimal > 0:
        residuo = decimal % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        pasos.append(f"{decimal} dividido por 16 da un cociente de {decimal // 16} y un residuo de {residuo} ({hex_chars[residuo]} en hexadecimal).")
        decimal = decimal // 16
    pasos.append(f"El número hexadecimal es {hexadecimal}.")
    return hexadecimal, pasos

def explicar_binario_a_decimal(binario):
    pasos = []
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        valor = int(binario[i]) * (2 ** (longitud - 1 - i))
        decimal += valor
        pasos.append(f"El dígito {binario[i]} en la posición {longitud - 1 - i} tiene un valor de {binario[i]} * 2^{longitud - 1 - i} = {valor}.")
    pasos.append(f"La suma de todos los valores es {decimal}.")
    return decimal, pasos

def explicar_hexadecimal_a_decimal(hexadecimal):
    pasos = []
    decimal = 0
    longitud = len(hexadecimal)
    for i in range(longitud):
        valor = int(hexadecimal[i], 16) * (16 ** (longitud - 1 - i))
        decimal += valor
        pasos.append(f"El dígito {hexadecimal[i]} en la posición {longitud - 1 - i} tiene un valor de {hexadecimal[i]} * 16^{longitud - 1 - i} = {valor}.")
    pasos.append(f"La suma de todos los valores es {decimal}.")
    return decimal, pasos

def explicar_binario_a_hexadecimal(binario):
    decimal, pasos_binario_a_decimal = explicar_binario_a_decimal(binario)
    hexadecimal, pasos_decimal_a_hexadecimal = explicar_decimal_a_hexadecimal(decimal)
    pasos = pasos_binario_a_decimal + ["Conversión de decimal a hexadecimal:"] + pasos_decimal_a_hexadecimal
    return hexadecimal, pasos

def explicar_hexadecimal_a_binario(hexadecimal):
    decimal, pasos_hexadecimal_a_decimal = explicar_hexadecimal_a_decimal(hexadecimal)
    binario, pasos_decimal_a_binario = explicar_decimal_a_binario(decimal)
    pasos = pasos_hexadecimal_a_decimal + ["Conversión de decimal a binario:"] + pasos_decimal_a_binario
    return binario, pasos

def main():
    print("Calculadora de conversión entre Binario, Decimal y Hexadecimal")
    print("1. Decimal a Binario")
    print("2. Decimal a Hexadecimal")
    print("3. Binario a Decimal")
    print("4. Hexadecimal a Decimal")
    print("5. Binario a Hexadecimal")
    print("6. Hexadecimal a Binario")
    
    opcion = int(input("Elige una opción (1-6): "))
    
    if opcion == 1:
        decimal = int(input("Ingresa un número decimal: "))
        resultado, pasos = explicar_decimal_a_binario(decimal)
        print(f"Binario: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    elif opcion == 2:
        decimal = int(input("Ingresa un número decimal: "))
        resultado, pasos = explicar_decimal_a_hexadecimal(decimal)
        print(f"Hexadecimal: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    elif opcion == 3:
        binario = input("Ingresa un número binario: ")
        resultado, pasos = explicar_binario_a_decimal(binario)
        print(f"Decimal: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    elif opcion == 4:
        hexadecimal = input("Ingresa un número hexadecimal: ")
        resultado, pasos = explicar_hexadecimal_a_decimal(hexadecimal)
        print(f"Decimal: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    elif opcion == 5:
        binario = input("Ingresa un número binario: ")
        resultado, pasos = explicar_binario_a_hexadecimal(binario)
        print(f"Hexadecimal: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    elif opcion == 6:
        hexadecimal = input("Ingresa un número hexadecimal: ")
        resultado, pasos = explicar_hexadecimal_a_binario(hexadecimal)
        print(f"Binario: {resultado}")
        print("Pasos para la conversión:")
        for paso in pasos:
            print(paso)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
