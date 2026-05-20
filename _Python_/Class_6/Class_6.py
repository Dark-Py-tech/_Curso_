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