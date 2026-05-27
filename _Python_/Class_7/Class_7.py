# # booleanos = [False, True]

# # # Tabla de verdad de and

# # print('x\ty\tx and y')
# # print('-'*22)
# # for x in booleanos:
# #     for y in booleanos:
# #         print(x, y, x and y, sep = '\t')
        
# # print()

# # # Tabla de verdad de or

# # print('x\ty\tx or y')
# # print('-'*22)
# # for x in booleanos:
# #     for y in booleanos:
# #         print(x, y, x or y, sep = '\t')

# # print()

# # # Tabla de verdad de ^ (or exclusivo)

# # print('x\ty\tx ^ y')
# # print('-'*21)
# # for x in booleanos:
# #     for y in booleanos:
# #         print(x, y, x ^ y, sep = '\t') 

# # print()

# # # Tabla de verdad de not

# # print('x\tnot x')
# # print('-'*13)
# # for x in booleanos:
# #     print(x, not x, sep = '\t')


# # &  (ampersand) - conjunción a nivel de bits.
# # |  (barra vertical) - disyunción a nivel de bits.
# # ~  (tilde) - negación a nivel de bits.
# # ^  (signo de intercalación) - o exclusivo a nivel de bits (xor).

# flag_register = 124

# print(format(flag_register, '#032b'))

# # ## Comprobar el estado del bit

# the_mask = 8 # el peso del bit es igual a 2 elevado a 3 (8) - tercer bit

# print(format(the_mask, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")

# # Reiniciar el bit a 0

# flag_register = flag_register & ~the_mask
# # flag_register &= ~the_mask # alternativa

# print("Cambiando tercer bit a cero")
# print(format(flag_register, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")
# # establecer el tercer bit a 1

# flag_register = flag_register | the_mask
# flag_register |= the_mask

# print("Estableciendo tercer bit a 1")
# print(format(flag_register, '#032b'))

# # Negación del tercer bit

# flag_register = flag_register ^ the_mask
# # # flag_register ^= the_mask # CUIDADO!!!, si ejecuto ambas instrucciones niega el bit dos veces!!!!

# print("Negando tercer bit")
# print(format(flag_register, '#032b'))

# flag_register ^= the_mask

# print("Negando de nuevo tercer bit")
# print(format(flag_register, '#032b'))


# #Desplazamientos

# valor = 2048

# for numero in range (5):
#    print(valor << numero) # Multiplica por 2

#    print(valor >> numero) # Divide por 2


#Listas

# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista:       ", numbers)  # Imprimiendo contenido de la lista original.

# numbers[0] = 111

# print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.

# print("Nuevo contenido de la lista: ", numbers)  # Imprimiendo el contenido de la lista actual.
 
# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# print("Recorriendo la lista con range(len(lista))")


# for indice in range(len(numbers)):
#     print("\tElemento en posición", indice, ":",numbers[indice])

# print("Recorriendo la lista con range(len(lista))")
    
# for elemento in numbers:
#     print("\t", elemento)

# del numbers[1]

# print("Longitud de la lista:", len(numbers))
# print(numbers)

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])
# # print(numbers[-5]) # falla

# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# # Paso 1: escribe una línea de código que solicite al usuario
# # reemplazar el número de en medio con un número entero ingresado por el usuario.
# print("Contenido del la lista", hat_list)

# centro = len(hat_list) // 2

# hat_list[centro] = int(input("Introduce el valor: "))

# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

# del hat_list[-1]

# # equivalente
# # del hat_list[len(hat_list - 1)]

# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
# print("Longitud actual de la lista:", hat_list)

# print("Contenido de la lista:", hat_list)
# print(hat_list)


# comandos para listas

# numbers.append("nuevo elemento al final")

# print(numbers)

# numbers.insert(1, "Nuevo valor en posición 1")

# print(numbers)

# numbers.remove("Nuevo valor en posición 1") 

# print(numbers)

#intercambiar variables

# variable_1 = 1
# variable_2 = 2
 
# variable_1, variable_2 = variable_2, variable_1
 
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list) 

#metodo reverse, ordena 

#my_list.reverse()

######################################

# my_list.reverse()

# print(my_list)

# ######################################

# my_list = ['Cesar', 'Alfredo', 'Cristina']

# for item in reversed(my_list):
#     print(item)

# for elemento in reversed(sorted(my_list)):
#     print(elemento)

# for elemento in my_list.__reversed__():
#     print(elemento)

#Lab 3.4.11

# Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

# La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.


# # paso 1
# beatles = []
# print("Paso 1:", beatles)

# # paso 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Paso 2:", beatles)

# # paso 3
# for number in range(2):
#     nombres = input("Introduce el nombre de los miembros: ")
#     beatles.append(nombres)

# print("Paso 3:", beatles)

# # paso 4

# beatles.remove("Stu Sutcliffe")
# beatles.remove("Pete Best")

# #alternativa

# del beatles[-1]
# del beatles[-1]

# print("Paso 4:", beatles)

# # paso 5
# beatles.insert(0,"Ringo Starr")
# print("Paso 5:", beatles)


# # probando la longitud de la lista
# print("Los Fav", len(beatles))

#ordenamiento burbuja

#Parcial
# my_list = [8, 10, 6, 2, 4]  # lista a ordenar

# print(my_list)

# for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
#     if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

# print(my_list)


#Completo
# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
# print(my_list)
# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
# print(my_list)

# #Intereactive

# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

# #metodo de ordenacion

# my_list.sort()