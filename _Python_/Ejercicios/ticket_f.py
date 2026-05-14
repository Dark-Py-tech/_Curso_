# ----------------------------------------
#             RECIBO DE VENTA             
# ----------------------------------------
# Producto:   COMIDA PARA MASCOTAS
# Cantidad:   2
# Precio U.:  12.99 €
# ----------------------------------------
# Subtotal:   25.98 €
# Descuento:  10.0% (-2.60 €)
# TOTAL:      23.38 €
# ----------------------------------------
#         ¡Gracias por su compra!         
# ----------------------------------------

anchura = 40
print("Bienvenido al sistema de ventas\n")
producto = (str(input(f"introduce el producto:" )))
cantidad = (int(input(f"Introduce Cantidad:")))
precio_unitario = (float(input(f"Precio por unidad: ")))
descuento = (float(input(f"Descuento: ")))
separador = "-" * anchura


print(separador)
print (f"{'RECIBO DE VENTA':^{anchura}}")
print(separador)
print (f'Producto : {producto.upper()}')
print (f'Cantidad : {cantidad}')
print (f'Precio U.: {precio_unitario:.2f} €')
print(separador)
subtotal = precio_unitario * int(cantidad)
print (f'Subtotal : {subtotal:.2f} €')
descuento_euros = subtotal * (descuento / 100)
print (f'Descuento: {descuento}% (-{descuento_euros:.2f} €)')
total = subtotal - descuento_euros
print (f'TOTAL    : {total:.2f} €')
print(separador)
print(f"{'¡Gracias por su compra!':^{anchura}}")
print(separador)



# ejemplo

# anchura = 40
# titulo = "RECIBO DE VENTA"
# producto_nombre = "comida para mascotas"

# # 1. Creamos el texto combinado
# linea_producto = f"Producto: {producto_nombre.upper()}"

# # 2. Imprimimos el diseño
# print("-" * anchura)
# print(f"{titulo:^{anchura}}")
# print("-" * anchura)
# print(f"{linea_producto:^{anchura}}")