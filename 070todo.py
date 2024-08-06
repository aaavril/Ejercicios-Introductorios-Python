"""Crear una función que convierta un número decimal entero positivo a hexadecimal o a binario dependiendo
de los parámetros. La función: convertir_decimal(numero, base), donde el parámetro numero es un
número entero positivo en base 10 y el parámetro base es un número que indica la base a la cual convertir
el número, solo puede tener el valor 2 o 16. Si se ingresa un número negativo o una base diferente a 2 o a
16, debe retornar una cadena vacia. Si la base es 16, debe retornar una cadena con el número convertido a
hexadecimal con el prefijo '0x' y si es base 2, debe retornar una cadena con el número convertido a binario
con el prefijo '0b'."""

"""
def convertir_decimal(numero, base):
    transformaciones= numero 
    binario= 0
    hexadecimal=0
    if numero<0 and base != 2 and base != 16:
        resultado= ""  
    elif base== 2:
        while transformaciones>0:
            binario= binario+ (transformaciones%2)
            transformaciones= transformaciones//2
        resultado= f"0b {binario}"         
    elif base== 16:
        resultado= f"0x {hexadecimal}"                 
    return resultado 

print (convertir_decimal(25,2))"""

def dec_binario (numero):
    numero_binario= ""
    while numero > 0:
        d= numero % 2
        numero= numero//2
        numero_binario= str(d) + numero_binario
    return "0n" + numero_binario

def dec_hex (numero):
    numero_hexa= ""
    while numero > 0:
        d= numero % 16
        numero= numero//16
        if d<= 9:
            numero_hexa= str(d) + numero_hexa
        elif d == 10:
            numero_hexa= "A" + numero_hexa
        elif d == 11:
            numero_hexa= "B" + numero_hexa    
        elif d == 12:
            numero_hexa= "C" + numero_hexa    
        elif d == 13:
            numero_hexa= "D" + numero_hexa   
        elif d == 14:
            numero_hexa= "E" + numero_hexa   
        elif d == 15:
            numero_hexa= "F" + numero_hexa        
    return "0x" + numero_hexa

def convertir_decimal(numero, base):
    cadena= "" 
    if numero >0 and (base==2 or base==16):
        if base==2:
            cadena= dec_binario(numero)
        elif base==16:
            cadena= dec_hex(numero)     
    return cadena 

print (convertir_decimal(250, 16))
print (convertir_decimal(250, 2))
print (convertir_decimal(250, 4))
print (convertir_decimal(-250, 16))
print (convertir_decimal(32, 16))
print (convertir_decimal(32, 2))