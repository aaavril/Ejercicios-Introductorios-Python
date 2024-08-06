'''¿Cómo modificaría el ejercicio anterior para que acepte que el usuario ingrese
cualquier tarifa?'''
TARIFA= float(input("ingrese la tarifa"))
DESCUENTO_3KG = 0.3
DESCUENTO_5KG = 0.5
peso_del_producto = float(input("Ingrese el peso del producto en kg: "))
    
if peso_del_producto < 0:
    print("El peso del producto no puede ser negativo")
else:
    if peso_del_producto < 3:
         monto_a_pagar = peso_del_producto * TARIFA
    elif peso_del_producto < 5:
        monto_a_pagar = peso_del_producto * TARIFA* (1 - DESCUENTO_3KG)
    else:
        monto_a_pagar = peso_del_producto * TARIFA* (1 - DESCUENTO_5KG)
    print("El monto a pagar es:", monto_a_pagar, "US$")