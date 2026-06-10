# ejemplo interactivo de listados e clientes, donde los datos como nombre, 
# apellido, email y teléfono se introducen de forma dinámica, 
# podéis usar una lista de duplas o una lista de diccionarios

lista_Clientes = []
#lista_cliente = {}
# print (type(lista_Clientes))


def add_clientes(nombre,apellido,email,ciudad,telefono):
    global lista_Clientes
    cliente = (nombre,apellido,email,ciudad,telefono)
    lista_Clientes.append(cliente)

def add_Client_dic(nombre, apellido, email, ciudad, telefono):
    cliente = {
        "Nombre": nombre, 
        "Apellido": apellido, 
        "Email": email, 
        "Ciudad": ciudad,
        "Telefono": telefono
    }
    return cliente

while True:
    nombre = input("Introduce Nombre: ")
    if nombre == '':
        break
    else:
        apellido = input("Introduce Apellido: ")
        email = input("Introduce email: ")
        ciudad = input("Introduce Ciudad: ")
        telefono = input("Introduce Telefono: ")

        #add_clientes(nombre,apellido,email,ciudad)
        #lista_Clientes.append (add_Client_dic)

    nuevo_cliente = add_Client_dic(nombre, apellido, email, ciudad)
    lista_Clientes.append(nuevo_cliente)

print (lista_Clientes)


# Version Compañero

# def nuevo():
#     datos = {}
#     datos["DNI"] = input("Introduce DNI: ")
#     datos["nombre"] = input("Introduce nombre: ")
#     datos["apellido"] = input("Introduce apellido: ")
#     datos["email"] = input("Introduce mail: ")
#     datos["telf"] = input("Itroduce teléfono: ")
#     clientes.append(datos)

# def eliminar():
#     dni = input("Introduce el DNI del registro a eliminar: ")
#     for i,n in enumerate(clientes):
#         if n["DNI"] == dni:
#             del clientes[i]
#             break

# def modificar():
#     dni = input("Introduce el DNI del registro a modificar: ")
#     for n in clientes:
#         if n["DNI"] == dni:
#             print(f'DNI: {n["DNI"]}\
#                     Nombre: {n["nombre"]}\
#                     Apellido: {n["apellido"]}\
#                     Email: {n["email"]}\
#                     Teléfono: {n["telf"]}')

#             opc = input("Introduce el dato a modificar (d/n/a/e/t): ")
#             nuevo = input ("Introduce nuevo valor: ")
#             if opc == "d":
#                 n["DNI"] = nuevo
#                 break
#             elif opc == "n":
#                 n["nombre"] = nuevo
#                 break
#             elif opc == "a":
#                 n["apellido"] = nuevo
#                 break
#             elif opc == "e":
#                 n["email"] = nuevo
#                 break
#             elif opc == "t":
#                 n["telf"] = nuevo
#                 break
#             else:
#                 print("Opció no valida")
#                 break
#     else:
#         print(f"DNI {dni} no encontrado")

# def mostrar():
#     dni = input("Introduce el DNI del registro a mostrar: ")
#     for n in clientes:
#         if n["DNI"] == dni:
#             print(f'DNI: {n["DNI"]}\
#                     Nombre: {n["nombre"]}\
#                     Apellido: {n["apellido"]}\
#                     Email: {n["email"]}\
#                     Teléfono: {n["telf"]}')
#             break
#     else:
#         print(f"DNI {dni} no encontrado")


# clientes = []
# while True:
#     print(
#         "1 - Nuevo Registro\n"
#         "2 - Eliminar Registro\n"
#         "3 - Modificar datos\n"
#         "4 - Mostrar datos\n"
#         "0 - Salir")
#     opcion = input("Introduce Opcion: ")
#     if opcion == "1":
#         nuevo()
#     elif opcion == "2":
#         eliminar()
#     elif opcion == "3":
#         modificar()
#     elif opcion == "4":
#         mostrar()
#     elif opcion == "0":
#         print("¡Adiós!")
#         break