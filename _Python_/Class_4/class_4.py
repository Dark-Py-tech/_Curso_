# # Triangulo

# # print("+" + (10 * "-") + "+")
# # print(("|" + (" " * 10) + "|\n") * 5, end="")
# # print("+" + (10 * "-") + "+")


# #interactivo
# #simbolo = "██"


# lado = int(input("Introduce el lado: "))
# alto = int(input("Introduce el altura: "))
# print("⬜️" * lado)
# print (("⬜️" + ("  " * (lado - 2)) + "⬜️\n") * (lado - 2), end="")
# print("⬜️" * lado)

# # ▫️
# # ◽️
# # ◻️
# # ⬜
# # ■

# anchura = int(input("Introduce la anchura del rectángulo: ")) -2
# altura = int(input("Introduce la altura del rectángulo: ")) -2

# cuadrado = "██"

# cabecera_pie = cuadrado + (anchura * cuadrado) + cuadrado

# print(cabecera_pie)
# print((cuadrado + ("  " * anchura + cuadrado) + "\n") * altura, end="")
# print(cabecera_pie)

# anchura = int(input("Introduce la anchura del rectángulo: "))
# altura = int(input("Introduce la altura del rectángulo: "))

# cuadrado = "██"
# espacio_central = "  " * (anchura - 2)

# cabecera_pie = cuadrado * anchura
# cuerpo_linea = cuadrado + espacio_central + cuadrado + "\n"

# cuerpo_total = cuerpo_linea * (altura - 2)

# print(cabecera_pie)
# print(cuerpo_total, end="")
# print(cabecera_pie)


#LAB 1 

# ingresa un valor flotante para la variable a aquí
# ingresa un valor flotante para la variable b aquí

# mostrar el resultado de la suma aquí
# mostrar el resultado de la resta aquí
# mostrar el resultado de la multiplicación aquí
# mostrar el resultado de la división aquí

# print("Programa operaciones\n")

# var_a = (float(input(" Introduce el Valor de la variable A: ")))
# var_b = (float(input(" Introduce el Valor de la variable B: ")))

# print("Suma: " + str(var_a+var_b))
# print("Resta: " + str(round(var_a-var_b,2)))
# print("Multiplicacion: " + str(var_a*var_b))
# print("Division: " + str(var_a/var_b))
# print("Resto: " + str(var_a%var_b))

# print("\n¡Eso es todo, amigos!")


#Lab 2

# print("Programa X\n")
# x = float(input("Ingresa el valor para x: "))

# # Escribe tu código aquí.
# valor = (1 / (x + (1 / (x + (1 / (x + (1 / x)))))))

# last= (x + (1 / x))
# mid = (x + (1 / last))
# first = (x + (1 / mid))
# y = (1 / first)

# print ()
# print("y =", y)
# print ("valor =", valor)


#lab 3

# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

# No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

# Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

hora = int(input("Introduce las horas:"))
minuto = int(input("Introduce las minuto:"))
tiempo = int(input("Introduce tiempo_Reunion:"))

horas = round((tiempo / 60),0)
minutos = round((tiempo % 60))

print ("horas", int(horas))
print ("minutos", int(minutos))


hora_fin = int((hora + horas))
minuto_fin = (minutos - minuto)

print ("hora final: " + str(hora_fin) + ":" + str(minuto_fin))

# soluciones

#lab_1
a = 0.1
b = 0.2

print(a + b)

# # Precisión exacta con el módulo Decimal
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')

resultado = a + b

#lab_2

print(resultado)  # Resultado: 0.3
x = float(input("Ingresa el valor para x: "))

resultado = 1 / ( x + 1 / ( x + 1 / (x + ( 1 / x))))

print("Resultado =", resultado)

#lab_3

hora = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_minutos = (minutos + dura)
hora = (hora + (total_minutos // 60)) % 24
minutos = total_minutos % 60

print(f"Hora actual: {hora:02}:{minutos:02}")


hora = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

duracion_total_en_minutos = (hora * 60 + minutos + duracion)
print(f'{(duracion_total_en_minutos // 60) % 24:02}:{duracion_total_en_minutos % 60:02}')

#Formato en print

# print(f'{})
