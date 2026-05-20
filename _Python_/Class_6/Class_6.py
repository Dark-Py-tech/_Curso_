# for numero in range(10): #final
#     print (numero)

# for numero in range(3, 10): #inicio y final
#     print (numero)

# for numero in range(3, 10, 2): #inicio, final e incremento
#     print (numero)

# for numero in range(10, 3, -2): #inicio, final e incremento con incremento negativo
#     print (numero)

# cadena = "Hola Mundo!"

# for letra in cadena:
#     print(letra)


import random

# numero_secreto = random.randint(1,10)
# intento = 0

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)


# while True:
#     numeros = input ("\nIntroduce el numero secreto !!! --> ")
#     numero = int(numeros)

#     intento += 1

#     if (numero == numero_secreto):
#         print ("¡Bien hecho, muggle! Eres libre ahora.\n")
#         break
#     else:
#         print ("¡Ja, ja! ¡Estás atrapado en mi bucle!\n")
 
# print (f"Numero de intentos {intento}")

# import random

# limite = int(input("Introduce el valor máximo del rango: "))

# # Genera un número secreto entre 1 y límite
# numero_secreto = random.randint(1, limite)
# intentos = 0

# print("¡Bienvenido al juego del número secreto!")

# while True:
#     numero = int(input("Intenta adivinar el número secreto: "))
#     intentos += 1

#     if numero == numero_secreto:
#         print(f"¡Bien hecho, muggle! Eres libre ahora.")
#         print(f"Has acertado en {intentos} intentos.")
#         break   # salimos del bucle
    
#     elif numero < numero_secreto:
#         print("¡Te has quedado corto!")

#     else:
#         print("¡Te has pasado!")


# # Melissa

# numero_secreto = random.randint(1, 10)
# intentos = 0
# adivinado = False

# print("He pensado un número entre 1 y 10. ¡Adivínalo!")

# while not adivinado:
#     intento = int(input("Introduce tu número: "))
#     intentos += 1

#     if intento < numero_secreto:
#         print("Más alto ")
#     elif intento > numero_secreto:
#         print("Más bajo ")
#     else:
#         adivinado = True
#         print(f"¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos ")

# valor1 = int(input("Introduce un primer numero para definir el rango: "))
# valor2 = int(input("Introduce un segundo numero para definir el rango: "))

# if valor1 > valor2:
#     valor1, valor2 = valor2, valor1

# print(f"Pensaré un número entre {valor1} y {valor2}.")

# numero_secreto = random.randint(valor1,valor2)

# while True:

#     try:
#         valor = input(f"Introduce un numero entre {valor1} y {valor2} a ver si aciertas el que he pensao (salir): ")

#         if valor.lower() == "salir":
#             print(f"Vaya, te has rendido, el numero era {numero_secreto}.")
#             break
# else:
#             valor = int(valor)
#             if valor == numero_secreto:
#                 print(f"Lo has adivinado, el numero es {valor}!!!!!!")
#                 break
#             elif valor > numero_secreto:
#                print(f"El numero secreto es menor que {valor}.") 
#             else:
#                 print(f"El numero secreto es mayor que {valor}.") 

#     except ValueError:
#         print("Error, el valor", valor, "no es un número válido. Inténtalo de nuevo.")

# import time

# for numero in range (1,6):
#     print (f"{numero} Mississippi")
#     time.sleep (1)

# print ("Lista o no, aquí vengo!")

#lab 3.2.9

# while True:
#     palabra = input ("\nInroduce la palabra secreta: ").lower()

#     if palabra == "chupacabra":
#         print ("Has dejado el bucle con éxito")
#         break

#lab 3.2.10

# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

# un bucle for;
# el concepto de ejecución condicional (if-elif-else).
# la sentencia continue.
# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
# Prueba tu programa con los datos que le proporcionamos.


# Datos de Prueba:
# Entrada de muestra:

# Gregory
# Salida esperada:

# Output
# G
# R
# G
# R
# Y
# Entrada de muestra:

# abstemious
# Salida esperada:

# Output
# B
# S
# T
# M
# S
# Entrada de muestra:

# IOUEA

# if letra in (‘AEIOU’):


# user_word = input("\nIntroduce la palabra: ").upper()

# for letra in user_word:
#     if letra in ("AEIOU"):
#         continue
#     else:
#         print (letra)

#lab 3.2.14

# Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.


# La figura ilustra la regla utilizada por los constructores:



# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.

# bloques = int(input("\nIntroduce el numero de Bloques: "))
# height = 0

# for numero in range (1,bloques):
#     if bloques == 0:
#         break
#     elif (bloques < numero):
#         break
    
#     bloques = bloques - numero
#     height += 1
#     sobrado = bloques

# print("La altura de la pirámide:", height)
# print("Sobran ", sobrado)

# Investigar el dibujar la piramide

#lab 3.2.15

# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

# Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.

# Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

# Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.

# Prueba tu código con los datos que hemos proporcionado.


# Datos de Prueba:
# Entrada de muestra:

# 15
# Salida esperada:

# Output
# 46
# 46
# 70
# 35
# 106
# 53
# 160
# 80
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# pasos = 17
# Entrada de muestra:

# 16
# Salida esperada:

# Output
# 8
# 4
# 2
# 1
# pasos = 4

#while True:

#mal

# numero = int(input("introduce un numero: "))
# pasos = 0
# while (numero > 1):
#     while numero % 2 == 0:
#         numero = numero / 2
#     else:
#         numero = 3 * numero + 1
#     print(f"{numero} \n")
#     pasos += 1
# else:
#     print(f"{numero} \n")

# #bien

# numero = int(input("introduce un numero: "))
# pasos = 0
# while (numero > 1):
#     if numero % 2 == 0:
#         numero = numero // 2
#     else:
#         numero = 3 * numero + 1
#     print(f"{numero} \n")
#     pasos += 1
    
# print(f"pasos = {pasos}")