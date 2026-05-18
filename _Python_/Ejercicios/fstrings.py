##########################
# Inserción de variables
##########################

# nombre = "Marta"
# edad = 35

# print(f"Hola {nombre}, tu edad es de {edad} años.")

# ##########################
# # Expresiones
# ##########################

# radio = 5
# print(f"El área del círculo es: {3.1416 * radio ** 2}")

# ##########################
# # Llamadas a métodos
# ##########################

# usuario = "Jorge"
# print(f"Nombre en mayúsculas: {usuario.upper()}")

# ##########################
# # Formato de números
# ##########################

# precio = 1250.4567

# # Redondear a 2 decimales (: .2f)
# print(f"Total: {precio:.2f} €") 

# # Separador de miles y 2 decimales
# print(f"Total formateado: {precio:,.2f} €")

# # # Porcentajes
# progreso = 0.756
# print(f"Progreso: {progreso:.1%}") # lo multipica por 100 automáticamente!

# ##########################
# # Alineación y espaciado
# ##########################

# productos = [("Higos", 1.2), 
#              ("Peras", 2.5), 
#              ("Manzanas", 4444.75)]

# for nombre, precio in productos:
#     print(f"{nombre:.<15} {precio:>10.2f} €")

# ##########################
# # Formato de fechas
# ##########################

# from datetime import datetime
# ahora = datetime.now()

# print(f"Hoy es: {ahora:%d/%m/%Y %H:%M}")

# ##############################
# # Autodepuración (python 3.8+)
# ##############################

# x = 10
# y = 20
# print(f"{x + y = }")

#############
# Ejercicio
#############

producto = input("Introduzca el nombre del producto: ")
cantidad = int(input("Introduzca la cantidad: "))
precio_unitario = float(input("Introduzca el precio unitario: "))
descuento_porcentaje = float(input("Introduzca el porcentaje de descuento: "))

subtotal = cantidad * precio_unitario
ahorro = subtotal * (descuento_porcentaje / 100)
total_final = subtotal - ahorro

linea = "-" * 40

print(linea)
print(f"{'RECIBO DE VENTA':^40}")
print(linea)
###########################################################
# Fecha centrada en anchura fija
from datetime import datetime

print(f"{f'Fecha: {datetime.now():%d/%m/%Y %H:%M}':^40}")
###########################################################

print(linea)

print(f"Producto:       {producto.upper()}")
print(f"Cantidad:       {cantidad}")
print(f"Precio U.:      {precio_unitario:.2f} €")
print(linea)

print(f"Subtotal:       {subtotal:.2f} €")
print(f"Descuento:      {descuento_porcentaje:.1f}% (-{ahorro:.2f} €)")
print(f"TOTAL:          {total_final:.2f} €")

print(linea)
print(f"{'¡Gracias por su compra!':^40}")
print(linea)



