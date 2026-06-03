# def message(number):
#     print("Ingresa un número:", number)

# number = 1234
# message(1)
# print(number)


# def message(what, number):
#     print("Ingresa", what, "número", number)
 
# message("teléfono", 11)
# message("precio", 5)
# message("cadena", "valor")

# def my_function(a,                              # obligatorio
#                 b,                              # obligatorio
#                 c = "Valor por defecto de c",   # opcional
#                 d = "Valor por defecto de d",   # opcional
#                 e = "Valor por defecto de e"):  # opcional
    
#     print(a, b, c, d, e, sep=' - ')
# ##############################
# # # por posición
# # print("Paso por posición:")
# # my_function(1, 2, 3, 4, 5)
# # my_function(1, 2, 3, 4)
# # my_function(1, 2, 3)
# # my_function(1, 2)
# # # my_function(1)              # falla
# # ##############################
# # # por palabra clave (por nombre)
# # print("\nPaso por palabra clave:")
# # my_function(a = "Valor de a", 
# #             # e = "valor de e",
# #             b = "valor de b", 
# #             c = "valor de c", 
# #             d = "valor de d")
# # ##############################
# # # por palabra clave (por nombre)
# # print("\nPaso por combinación:")

# # my_function(1, 
# #             2,
# #             e = "valor de d")

# # def happy_new_year(wishes = True):
# #     print("Tres...")
# #     print("Dos...")
# #     print("Uno...")
# #     if not wishes:
# #         return
 
# #     print("¡Feliz año nuevo!")


# # def list_sum(lst):
# #     s = 0
 
# #     for elem in lst:
# #         s += elem
 
# #     return s

# # print(list_sum([5, 4, 3]))

# # def strange_list_fun(n):
# #     strange_list = []
    
# #     for i in range(0, n):
# #         strange_list.insert(0, i)
    
# #     return strange_list

# # print(strange_list_fun(5))

# #4.3.4   LAB   Un año bisiesto: escribiendo tus propias funciones

# # Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

# # La semilla de la función ya se muestra en el código esqueleto del editor.

# # Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

# # El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

# def es_anyo_bisiesto(anyo):
#     anyo = int(anyo)

#     if (anyo < 1582 or anyo < 0):
#         print ("\033[31mAño no pertenece al calendario Gregoriano (1582 en adelante)")
#     else:
#         if ((anyo % 4) != 0):
#             #print (f"Año {anyo} \033[33mNo Bisiesto")
#             return False
#         elif ((anyo % 100) != 0):
#             #print (f"Año {anyo} \033[31mBisiesto")
#             return True
#         elif ((anyo % 400) != 0):
#             #print (f"Año {anyo} \033[33mNo Bisiesto")
#             return False
#         else:
#             #print (f"Año {anyo} \033[31mBisiesto")
#             return True

# # test_data = [1900, 2000, 2016, 1987]
# # test_results = [False, True, True, False]
# # for i in range(len(test_data)):
# #     yr = test_data[i]
# #     print(yr,"->",end="")
# #     result = es_anyo_bisiesto(yr)
# #     if result == test_results[i]:
# #         print("OK")
# #     else:
# #         print("Fallido")

# # 4.3.5   LAB   Cuántos días: escribiendo y usando tus propias funciones
# # Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# # La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# # Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.4). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

# # Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

# def days_in_month(anyo, meses):
#     mes_normal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     mes_bisiesto = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     #mes = [0, 31, 29 if es_anyo_bisiesto(anyo) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # esto evita el if
    
#     if (es_anyo_bisiesto(anyo) == True ) :
#         return mes_bisiesto[meses]
#     else:
#         return mes_normal[meses]
    
#     #return mes[meses]

# # test_years = [1900, 2000, 2016, 1987]
# # test_months = [2, 2, 1, 11]
# # test_results = [28, 29, 31, 30]
# # for i in range(len(test_years)):
# #     yr = test_years[i]
# #     mo = test_months[i]
# #     print(yr, mo, "->", end="")
# #     result = days_in_month(yr, mo)
# #     if result == test_results[i]:
# #         print("OK")
# #     else:
# #         print("Fallido")

# # 4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones
# # Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# # Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.

# def day_of_year(anyo, meses, dia):
#     suma_dias=0
    
#     # dias = [0, 31, 29 if es_anyo_bisiesto(anyo) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # esto evita el if

#     # for i in range(1, meses):
#     #     suma_dias += dias[i]

#     for j in range (meses):
#         suma_dias += days_in_month(anyo, j)

#     return suma_dias + dia

# print(day_of_year(2000, 3, 1))

# 4.3.7   LAB   Números primos - cómo encontrarlos
# Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

# ¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).

# Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.

# Tu tarea es escribir una función que verifique si un número es primo o no.

# La función:

# se llama is_prime;
# toma un argumento (el valor a verificar)
# devuelve True si el argumento es un número primo, y False de lo contrario.
# Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica el resto - si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener el proceso.

# Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **. Recuerda: la raíz cuadrada de x es lo mismo que x0.5.

# Complementa el código en el editor.

# Ejecuta tu código y verifica si tu salida es la misma que la nuestra.

# Salida esperada:

# Output
# 2 3 5 7 11 13 17 19

# def is_prime(num):
#     if num < 2:
#         return False
    
#     for i in range(2, num):
#         if (num % i == 0):
#             return False
            
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# 4.3.8   LAB   Conversión del consumo de combustible
# El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

# En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

# Las funciones:

# se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)
# Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma que la nuestra.

# Aquí hay información para ayudarte:

# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.
# Salida esperada:

# Output
# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757

# def liters_100km_to_miles_gallon(liters):
#     millas = 100 * 1000 / 1609.344

#     return 100 * 3.785411784 / (liters * 1.609344)

# def miles_gallon_to_liters_100km(miles):
#     km = miles * 1609.344 / 1000 / 100

#     return 100 * 3.785411784 / (miles * 1.609344)

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


