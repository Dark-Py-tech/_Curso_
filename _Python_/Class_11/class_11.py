#cesar.martin@numaconsulting.com

# aquí podeis ver el roadmap de py https://pythoninstitute.org/certification-tracks

# value = ''
# try:
#     value = input('Ingresa un número natural: ')
#     value = int(value)
#     print('El recíproco de', value, 'es', 1/value)

# except ValueError:
#     print('No podemos convertir a entero el valor', value)

# except ZeroDivisionError:
#     print('La división entre cero no está permitida en nuestro Universo.')

# except Exception:
#     print("Vamos a registrar esto en un log")
# else: 
#   printf("Se ejecvyte si no hay error") 
# finally: 
#   printf ("Se ejecuta simepre")


#--------------------------------------------------------
#Para recorrer las excepciones

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)

# print_exception_tree(BaseException)
#---------------------------------------------------------


# value = ''
# while True:
#     try:
#         value = input('Ingresa un número natural: ')
#         value = int(value)

#         if value < 0:
#             print("Debe ser un número natural.")
#             continue

#         print('El recíproco de', value, 'es', 1/value)
#         break

#     except ValueError:
#         print('No podemos convertir a entero el valor', value)

#     except ZeroDivisionError:
#         print('La división entre cero no está permitida en nuestro Universo.')

#     except Exception:
#         print("Vamos a registrar esto en un log")

# match opcion:
#     case "1":
#         nuevo()
#     case "2":
#         eliminar()
#     case "3":
#         modificar()
#     case "4":
#         mostrar()
#     case "0":
#         print("¡Adiós!")
#         break
#     case _:
#         print("Opción no válida")


#guardos exceptions en log

# import logging

# # Configuración del logging
# logging.basicConfig(
#     filename='aplicacion.log',
#     filemode='w' - # # modo de escitura 
#     level=logging.WARNING,
#     format='%(asctime)s - %(levelname)s - %(message)s'
#     encoding='utf-8'
# )

# value = ''

# try:
#     value = input('Ingresa un número natural: ')
#     value = int(value)

# except ValueError as e:
#     print('No podemos convertir a entero el valor', value)
#     logging.error(
#         "Error de conversión. Valor introducido: '%s'. Detalle: %s",
#         value,
#         e
#     )

# except ZeroDivisionError as e:
#     print('La división entre cero no está permitida en nuestro Universo.')
#     logging.error("Intento de división por cero. Detalle: %s", e)

# except Exception:
#     print("Ha ocurrido un error inesperado.")
#     logging.exception("Excepción no controlada")

# else:
#     print('El recíproco de', value, 'es', 1 / value)

# finally:
#     print("Siempre se ejecuta el bloque finally")