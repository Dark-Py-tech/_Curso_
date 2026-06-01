# class Cliente:
#     def __init__(self, nombre, apellido, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.email = email

#     def __str__(self):
#         return f"Cliente(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
#     def __repr__(self):
#         return f"Cliente(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"

# ######################################################

# # Crear una instancia
# cliente1 = Cliente(
#     nombre="Juan",
#     apellido="Pérez",
#     email="juan.perez@example.com"
# )


# lista1 = [1, 2, 3, cliente1]

# lista2 = [cliente1, 33, 44, 55]

# cliente1.nombre = "César"
# class Cliente:
#     def __init__(self, nombre, apellido, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.email = email

#     def __str__(self):
#         return f"Cliente(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
#     def __repr__(self):
#         return f"Cliente(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"

# ######################################################

# # Crear una instancia
# cliente1 = Cliente(
#     nombre="Juan",
#     apellido="Pérez",
#     email="juan.perez@example.com"
# )


# lista1 = [1, 2, 3, cliente1]

# lista2 = [cliente1, 33, 44, 55]

# cliente1.nombre = "César"   ###################### 

# print(lista1)

# print(lista2)

# print(cliente1)


# ###################

# def modificar_cliente(cliente):
    
#     cliente.nombre="Otro nombre"

# #####################

# modificar_cliente(cliente1)

# print(cliente1)


# my_list = [1, 3, 11, 5, 1, 17, 7, 15, 13]
# largest = my_list[0]


# # for i in range(1, len(my_list)):
# for i in range(1, len(my_list)):

#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)
# ##########################

# my_list = [1, 3, 11, 5, 1, 17, 7, 15, 13]
# largest = my_list[0]

# for elemento in my_list[1:]:

#     if elemento > largest:
#         largest = elemento

# print(largest)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 555

# for indice in range(len(my_list)):
    
#     if my_list[indice] == to_find:
#         print("Elemento encontrado en el índice", indice)
#         break
# else:
#     print("El elemento no se ha encontrado en la lista")
# ########################3
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break

# if found:
#     print("Elemento encontrado en el índice", i)
# else:
#     print("ausente")

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
 
# for number in bets:
#     if number in drawn:
#         hits += 1
 
# print(hits)

#3.6.6

# Imagina una lista - no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

# Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

# Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

# Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.

# No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list_2 = []

# for element in my_list:
#     if element not in my_list_2:
#         my_list_2.append(element)

# print("La lista con elementos únicos:")
# print(my_list_2)

# ####################################################################
# # solución creando una nueva lista con elementos únicos
# ####################################################################
# mi_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# nueva_lista = []
# for numero in mi_lista:                 # Recorremos todos los números de la lista original.
#     if numero not in nueva_lista:       # Si el número no aparece dentro de la nueva lista ...
#         nueva_lista.append(numero)      # ... añadirlo aquí.
# mi_lista = nueva_lista                  # Asignamos la nueva lista a la variable original.
# del nueva_lista                         # y eliminamos la lista temporal 
# print("La lista con elementos únicos:")
# print(mi_lista)
# ####################################################################
# ## Alternativa 1
# ####################################################################

# mi_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# nueva_lista = []

# for elemento in mi_lista:
#     if elemento in nueva_lista:
#         continue
#     nueva_lista.append(elemento)
# print(nueva_lista)
# ####################################################################
# ## Alternativa sin usar una nueva lista!!! (poco eficiente por los bucles anidados)
# ####################################################################

# mi_lista = [1, 2, 4, 4, 1, 44, 10, 2, 44, 6, 6, 2, 9, 10, 10, 44]
# mi_lista.sort()
# contador=0

# for numero in mi_lista:
#     while numero in mi_lista[contador + 1 : ]:
#         mi_lista.remove(numero)
#     contador +=1
# print("La lista con elementos únicos:")
# print(mi_lista)
# ####################################################################
# ## Alternativa sin usar una nueva lista!!! (más eficiente)
# ####################################################################

# mi_lista = [1, 2, 4, 4, 1, 44, 10, 2, 44, 6, 2, 9, 10, 44]
# mi_lista.sort()

# # Recorremos desde el último elemento hasta el segundo (índice 1)
# for i in range(len(mi_lista) - 1, 0, -1):
#     if mi_lista[i] == mi_lista[i - 1]:
#         del mi_lista[i]

# print("Únicos recorriendo al revés:", mi_lista)
# ####################################################################
# ## Alternativa sin usar una nueva lista!!! (más eficiente y sin ordenar)
# ####################################################################

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 2, 1]
# i = 0

# while i < len(my_list):
#     if my_list.count(my_list[i]) > 1:
#         my_list.remove(my_list[i])
#     else:
#         i += 1

# print(my_list)

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 2]
# print("La lista con números duplicados")
# print(my_list)
# pos = 0
# while pos < len(my_list):
   
#     elemento = my_list[pos]
    
#     if my_list[pos] in my_list[pos+1:]:
       
#         my_list.remove(elemento)
        
#     else:
#         pos += 1
   
# print("La lista con elementos únicos:")
# print(my_list)



# sample_list = ["A", "B", "C", "D", "E"]
# new_list = sample_list[0:1] + sample_list[-1:]
# print(new_list)  # output: ['C', 'D']

# my_list = [1, 2, "in", True, "ABC"]

# print(1 in my_list)             # output True
# print("A" not in my_list)       # output True
# print(3 not in my_list)         # output True
# print(False in my_list)         # output False


# row = []

# for i in range(8):
#     row.append(WHITE_PAWN)

# row = [WHITE_PAWN for i in range(8)]

# squares = [x ** 2 for x in range(10)]

# print (squares)

# odds = [x for x in squares if x % 2 != 0 ]

# board = []

# for i in range(8):
#     row = ["" for i in range(8)]
#     board.append(row)

# filas = int(input("¿Cuántas filas quieres crear? "))
# columnas = int(input("¿Cuántas columnas quieres crear? "))

# # matriz = []

# # for fila in range(filas):
# #     matriz.append([])               # crea una lista vacía por cada fila

# #     for columna in range(columnas):
# #         matriz[fila].append(str(fila) + "-" + str(columna))


# matriz = [[str(fila) + "-" + str(columna) for columna in range(columnas)] for fila in range(filas)]



# # #  Impresión de la matriz con formato

# for fila in range(len(matriz)):
#     print() 
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end =" ")


#Ajedrez

# EMPTY = "--------"
# PAWN = "PEON"
# TORRE = "TORRE"
# CABALLO = "CABALLO"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = TORRE
# board[0][7] = TORRE
# board[7][0] = TORRE
# board[7][7] = TORRE
# board[7][1] = CABALLO
# board[7][6] = CABALLO
# board[7][2] = "ALFIL"
# board[7][5] = "ALFIL"
# board[7][3] = "REINA"
# board[7][4] = "REY"

# for row in board:
#     print()
#     for cell in row:
#         print(format(cell.center(8),"8"), end =" ")

#otro ajedrez

# EMPTY = "--------"
# PAWN = "PEON"
# TORRE = "TORRE"
# CABALLO = "CABALLO"

# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = TORRE
# board[0][7] = TORRE
# board[6] = ["PEON" for i in range(8)]
# board[7] = [TORRE, CABALLO, "ALFIL", "REINA", "REY", "ALFIL", CABALLO, TORRE]
# # board[7][0] = TORRE
# # board[7][7] = TORRE
# # board[7][1] = CABALLO
# # board[7][6] = CABALLO
# # board[7][2] = "ALFIL"
# # board[7][5] = "ALFIL"
# # board[7][3] = "REINA"
# # board[7][4] = "REY"

# for row in board:
#     print()
#     for cell in row:
#         print(format(cell.center(8),"8"), end =" ")


# temperatura

# import random

# temps = [[0.0 for h in range(24)] for d in range(31)]

# total = 0.0

# # # Rellenar con valores aleatorios

# for fila in range(len(temps)):
#     for columna in range(len(temps[fila])):
#         temps[fila][columna] = random.choice(range(10, 450))/10

# for day in temps:
#     total += day[11] # Las 12:00 horas

# average = total / 31

# print("Temperatura promedio al mediodía:", round(average,1), "grados centígrados")
        
# #Imprimir lista con formato

# for fila in range(len(temps)):
#     print("\nDía", fila + 1)
#     for columna in range(len(temps[fila])):
#         print(temps[fila][columna], end = "  ")
     

# print()
# highest = -100.0

# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
            
# print("La temperatura más alta fue de", highest, "grados")

# # #  Días con temperatura superior a 20 grados a las 12 del mediodía

# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1

# print(hot_days, "fueron los días calurosos.")

# #Habitaciones

# rooms = [[[False for habitacion in range(20)] for planta in range(15)] for edificio in range(3)]

# rooms[1][9][13] = True

# rooms[0][4][1] = False

# # # ##  Habitaciones ocupadas en la planta 15 del tercer hotel

# rooms[2][14][0] = True    # Edificio 3, Planta 15, Habitación 1
# rooms[2][14][1] = True    # Edificio 3, Planta 15, Habitación 2

# vacancy = 0

# # #  Número de habitaciones libres en la planta 15 del tercer hotel

# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1

# print("Hay", vacancy, "habitaciones libres en la planta 15 del tercer edificio")