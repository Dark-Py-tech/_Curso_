# ejemplo interactivo de listados e clientes, donde los datos como nombre, 
# apellido, email y teléfono se introducen de forma dinámica, 
# podéis usar una lista de duplas o una lista de diccionarios

lista_Clientes = []
# print (type(lista_Clientes))

def add_clientes(nombre,apellido,email,ciudad):
    global lista_Clientes
    cliente = (nombre,apellido,email,ciudad)
    lista_Clientes.append(cliente)

while True:
    nombre = input("Introduce Nombre: ")
    if nombre == '':
        break
    else:
        apellido = input("Introduce Apellido: ")
        email = input("Introduce email: ")
        ciudad = input("Introduce Ciudad: ")

        add_clientes(nombre,apellido,email,ciudad)

print (lista_Clientes)