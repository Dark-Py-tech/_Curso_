#Ejemplo condicional IF

# valor = int(input("Introduce un valor numérico: "))

# if valor > 0:
#     print("El valor de ", valor, "es positivo")    
#     print("Esto es otro mensaje dentro del if")
# else:
#     print("El valor de ", valor, "es negativo o igual a cero")    

# print("Esto se ejecutará siempre")

# tiempo = input(("Que tiempo hace? "))

# if (tiempo == "bueno"):
#     print ("vamos a caminar")
# elif (tiempo == "malo"):
#     print ("vamops al teatro")
# else:
#     print ("Nos Quedamos en casa a Netflix + Sofa")

# ejercicio

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

# if (input(("el tiempo es ? ")).lower == "bueno"):
#     if (input(("Conozco un buen restaurante? ")).lower == "si"):
#         print("vamos a comer")
#     else:
#         print(" Comemos un sandwich")
# else:
#     if (input(("Vamos al teatro, tenemos entradas? ")).lower == "si"):
#         print ("Vamos al teatro")
#     else:
#         print ("vamos de compras")

# tiempo = input("¿Qué tiempo hace hoy? (bueno o malo): ").lower()

# if tiempo == "bueno":

#     conoce_restaurante = input("\t¿Conoces algún buen restaurante? (si o no): ").lower()

#     if conoce_restaurante == "si":

#         print("\t\t¡Genial, nos vamos a comer al restaurante!")
#     else:
#         print("\t\t¡Entonces nos comeremos un sandwich!")
# else:

#     hay_entradas = input("\t¿Hay entradas disponibles para ir al teatro? (si o no): ")

#     if hay_entradas == "si":
#         print("\t\t¡Genial, nos vamos al teatro!")
#     else:
#         print("\t\t¡Entonces nos vamos de compras!")

# bucles

# numero = 1

# while (numero <= 10):

#     print(numero)
#     numero += 1         # incremento de 1 por iteración

# ############################################

# numero = 1

# while True:

#     print(numero)
#     numero += 1

#     if numero > 10:
#         break           # Interrupción del bucle

#ejerciop

#valor 1 al 100 impar

# numero = 1

# while numero<101:
#     print (numero)
#     numero += 2


# print("otro")

# numero = 1

# while (numero<101):
#     if (numero//2) != 0:
#         print (numero)
#   numero += 1

# print("otro 1 ")

# numero = 1

# while (numero<100):
#     #nn = (numero%2)
#     #print ("valor de resultado", nn)
#     if (numero%2) != 0:
#         print ("valor del numero" , numero)
#     numero += 1

# numero = 0

# while True:
#     if (numero >=100):
#         break
#     elif ((numero%2) != 0):
#         print ("valor del numero" , numero)
#     numero += 1

#Dinamico

# numero1 = int(input("Introduce el primero numero: "))
# numero2 = int(input("Introduce el primero numero: "))

# while (numero1<numero2):
#     if (numero1%2) != 0:
#         print ("valor del numero" , numero1)
#     numero1 += 1


#excepciones

# while True:

#     try:
#         valor = input("Introduce un valor numérico: ")

#         valor = int(valor)

#         print("El número introducido es:", valor)    
    
#         break

#     except ValueError:

#         print("Error, el valor", valor, "no es un número válido. Inténtalo de nuevo.")
# valor = input("Introduce un valor numérico: ")

#otra forma con el isdigit()

# if valor.isdigit():
#     valor = int(valor)


#valor de numero mayor introducido

# mayor = None

# while True:
#     entrada = input("Por favor, introduce un número entero válido o la palabra 'salir' para terminar: ")
    
#     # Comprobamos la condición de salida del bucle
#     if entrada.lower() == "salir":
#         break
    
#     # Ahora podemos convertir a número
#     numero = int(entrada)
        
#     # Si es el primer número que se introduce, o si es mayor que el que ya teníamos, lo guardamos
#     if mayor is None or numero > mayor:
#         mayor = numero
            
# ################################################################################

# # Fuera del bucle, mostramos el resultado si se introdujo al menos un número
# if mayor is not None:
#     print(f"\nEl número mayor de todos los introducidos es: {mayor}")
# else:
#     print("\n¡No has introducido ningún número!")

#lab 3.1.10

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
# Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un Espatifilo también!

# planta = input("Introduce la planta: ")

# if (planta == "ESPATIFILIO"):
#     print ("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
# elif (planta == "espatifilo"):
#     print ("No, ¡quiero un gran Espatifilo!")
# else:
#     print (f'¡Espatifilo!, ¡No {planta}!')


#lab 3.1.11

# Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

# si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
# Tu tarea es escribir una calculadora de impuestos.

# Debe aceptar un valor de punto flotante: el ingreso.
# A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
# Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

# Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.

# Prueba tu código con los datos que hemos proporcionado.


# Datos de Prueba
# Entrada de muestra:

# 10000
# Salida esperada:

# Output
# El impuesto es: 1244.0 pesos
# Entrada de muestra:

# 100000
# Salida esperada:

# Output
# El impuesto es: 19470.0 pesos

# pago = float(0.0)
# limite = 85528
# porcentaje_superior = 32
# porcentaje_inferior = 18
# impuesto_base = 14839.2
# impuesto_minimo = 556.2

# while True:
#         ingreso = input("Introduce el Sueldo: ")
#         try:
#             ingreso_float = float (ingreso)
        
#             if (ingreso_float > limite):
#                 primer_ingreso= ingreso_float - limite
#                 valor_impuesto = (impuesto_base + ((primer_ingreso * porcentaje_superior) / 100))
#                 pago = round(valor_impuesto, 0)
#             else:
#                 pago = round((((ingreso_float * porcentaje_inferior) / 100) - impuesto_minimo), 0)
#                 if (pago <= 0.0):
#                     pago = 0.0 

#             print (f"El impuesto es: {pago} Euros")
#             break
#         except ValueError:
#              print ("Error: Entrada no válida. Ingrese un valor númerico\n")             



#lab 3.1.12

# Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

# Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# si el número del año no es divisible entre cuatro, es un año común.
# de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# de lo contrario, si el número del año no es divisible entre 400, es un año común.
# de lo contrario, es un año bisiesto.
# Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.


# El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.

# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

# Prueba tu código con los datos que hemos proporcionado.


# Datos de Prueba:
# Entrada de muestra:

# 2000
# Salida esperada:

# Output
# Año bisiesto

# Entrada de muestra:

# 2015
# Salida esperada:

# Output
# Año comun

# while True:
#     anyo = input("Introduce el año para verificar si es Bisiesto: ")
#     anyos = anyo.isdigit()

#     while (anyos == True):
#         anyos = False
#         anyo = int(anyo)

#         if (anyo < 1582 or anyo < 0):
#             print ("Año no pertenece al calendario Gregoriano (1582 en adelante)")
#         else:
#             if ((anyo % 4) != 0):
#                 print (f"Año {anyo} No Bisiesto")
#             elif ((anyo % 100) != 0):
#                 print (f"Año {anyo} Bisiesto")
#             elif ((anyo % 400) != 0):
#                 print (f"Año {anyo} No Bisiesto")
#             else:
#                 print (f"Año {anyo} Bisiesto")         
#     break
