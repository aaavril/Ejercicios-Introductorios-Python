''' La empresa MiTienda cobra sus envíos según el peso de los productos. En los
envíos para Uruguay, la tarifa es de 21.99 US$ por kg. La empresa ofrece un 30% de
descuento a partir del 3kg y un 50% de descuento a partir del 5kg. Escriba un
algoritmo en pseudocódigo que dado el peso indique el monto a pagar. '''

TARIFA_BASE_URUGUAY = 21.99
DESCUENTO_3KG = 0.3
DESCUENTO_5KG = 0.5
peso_del_producto = float(input("Ingrese el peso del producto en kg: "))
    
if peso_del_producto < 0:
    print("El peso del producto no puede ser negativo")
else:
    if peso_del_producto < 3:
         monto_a_pagar = peso_del_producto * TARIFA_BASE_URUGUAY
    elif peso_del_producto < 5:
        monto_a_pagar = peso_del_producto * TARIFA_BASE_URUGUAY * (1 - DESCUENTO_3KG)
    else:
        monto_a_pagar = peso_del_producto * TARIFA_BASE_URUGUAY * (1 - DESCUENTO_5KG)
    print("El monto a pagar es:", monto_a_pagar, "US$")
