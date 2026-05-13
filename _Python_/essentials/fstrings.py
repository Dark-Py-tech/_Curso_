
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings

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

# # Porcentajes
# progreso = 0.756
# print(f"Progreso: {progreso:.1%}")

# ##########################
# # Alineación y espaciado
# ##########################

# productos = [("Higos", 1.2), ("Peras", 2.5), ("Manzanas", 4.75)]

# for nombre, precio in productos:
#     print(f"{nombre:.<15} {precio:>5.2f} €")

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

