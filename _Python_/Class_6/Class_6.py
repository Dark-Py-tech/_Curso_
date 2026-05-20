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

numero_secreto = random.randint(1,10)
intento = 0

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")


while True:
    numeros = input ("\nIntroduce el numero secreto !!! --> ")
    numero = int(numeros)

    intento += 1

    if (numero == numero_secreto):
        print ("¡Bien hecho, muggle! Eres libre ahora.\n")
        break
    else:
        print ("¡Ja, ja! ¡Estás atrapado en mi bucle!\n")
 
print (f"Numero de intentos {intento}")

