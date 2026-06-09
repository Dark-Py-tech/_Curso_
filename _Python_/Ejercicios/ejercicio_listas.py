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