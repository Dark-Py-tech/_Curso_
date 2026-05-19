#https://drive.google.com/file/d/1CU5mmuuTdKdU7TWb84u-O3SVMPUbkhIh/view?usp=drive_link
#https://drive.google.com/file/d/1_7YZ-z7eOle7IPxmWKlE-wdk4Xfk-aRA/view?usp=drive_link

# print("Estoy" + '\n\"\"aprendiendo\"\"\n' + '"""Python"""')
# print()
# print("Estoy" + '\n\"\"aprendiendo\"\"\n' + '\"\"\"Python\"\"\"')
# print()
# print("Estoy" ,'\"\"aprendiendo\"\"' , '\"\"\"Python\"\"\"', sep="\n")

# print(' "Estoy"\n','""aprendiendo""\n','"""Python"""')

# print('"Estoy"',
#       '""aprendiendo""',
#       '"""Python"""',
#       sep = '\n')

# print()

# print("\"Estoy\"",
#       "\"\"aprendiendo\"\"",
#       "\"\"\"Python\"\"\"",
#       sep = "\n")

# print()

# print('''"Estoy"
# ""aprendiendo""
# """Python"""''')

# print()

# print('''\"Estoy"''',
# '''\"\"aprendiendo""''',
# '''\"""Python"""''', sep="\n")

# print('"Estoy"\n""aprendiendo""\n"""Python"""')

# print('"Estoy"\n','""aprendiendo""\n','"""Python"""')

# print('"Estoy"','""aprendiendo""','"""Python"""', sep = "\n")

# print('''""Estoy""\n""aprendiendo""\n"""Python"""''')

# print("\"Estoy\"", "\"\"aprendiendo\"\"", "\"\"\"Python\"\"\"", sep="\n")

# print(1*'"' + "Estoy" + 1 * '"' , 2 * '"' + "aprendiendo" + 2 * '"' , 3 * '"' + "python" + 3 * '"' ,sep="\n")

# comilla_doble = '"'

# print(1 * comilla_doble + "Estoy" + 1 * comilla_doble, 
#       2 * comilla_doble + "aprendiendo" + 2 * comilla_doble, 
#       3 * comilla_doble + "python" + 3 * comilla_doble,
#       sep="\n")

# print((comilla := '"') + "Estoy" + comilla * 1,
#       comilla * 2 + "aprendiendo" + comilla * 2,
#       comilla * 3 + "Python" + comilla * 3,
#       sep='\n'  )

# #type(variable) - devuelve <class 'str'>, <class 'int'>, <class 'float'>, etc. dependiendo del tipo de dato que sea la variable.
# #para scar solo el tipo de variable podemos hacer type(variable).__name__ - devuelve 'str', 'int', 'float', etc. dependiendo del tipo de dato que sea la variable.

# import sys
# sys.set_int_max_str_digits(0)
   

# manzanas_john = 3
# manzanas_mary = 5
# manzanas_adam = 6
# manzanas_total = 0


# print("\nManzanas de John:", manzanas_john, "\n")
# print("Manzanas de Mary:", manzanas_mary, "\n")
# print("Manzanas de Adam:", manzanas_adam, "\n")
# manzanas_total = manzanas_john + manzanas_mary + manzanas_adam
# print("Total de manzanas:", manzanas_total)
# print()
# manzanas_total = manzanas_john * manzanas_mary * manzanas_adam
# print("Total de manzanas:", manzanas_total)
# print()
# manzanas_total = manzanas_john ** manzanas_mary ** manzanas_adam
# print("Total de manzanas:", manzanas_total)
# print()
# manzanas_total = manzanas_john / manzanas_mary / manzanas_adam
# print("Total de manzanas:", manzanas_total)
# print()
# manzanas_total = manzanas_john // manzanas_mary // manzanas_adam
# print("Total de manzanas:", manzanas_total)


# manzanas_juan, manzanas_maria, manzanas_adan = 3, 5, 6  # desempaquetado de tuplas

# # alternativa
# manzanas_juan = 3
# manzanas_maria = 5
# manzanas_adan = 6

# # Imprimir las manzanas de cada uno

# print(manzanas_juan, 
#       manzanas_maria, 
#       manzanas_adan, 
#       sep=", " )

# # Alternativa
# print(str(manzanas_juan) + ", " + str(manzanas_maria) + ", " + str(manzanas_adan))

# # Calcular la suma
# total_manzanas = (manzanas_juan + manzanas_maria + manzanas_adan)

# # Imprimir el total de manzanas
# print(total_manzanas)

# # Alternativa
# print("Número total de manzanas:", total_manzanas)

# # alternativa
# print("Número total de manzanas: " + str(total_manzanas))

# valor_numerico = 10

# valor_numerico = valor_numerico * 2 + 10

# print(valor_numerico)

# #############################################

# valor_numerico = 10

# valor_numerico *= 2 + 10

# print(valor_numerico)



# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


x = 0
x = float(x)
#3x3 - 2x2 + 3x - 1
y = (3 * x**3) - (2 * x**2) + (3 * x - 1)
# Escribe tu código aquí.
print("y =", y)

# "¡El apocalipsis zombie ha llegado! Eres el encargado de suministros de un refugio. 
# Tu misión es crear un programa que calcule cuánto tiempo podrá sobrevivir un grupo de personas con los recursos actuales."
# Instrucciones del ejercicio
# Define las siguientes variables con valores inventados:
# personas: Número de personas en el refugio.
# raciones_por_persona: Cuántas raciones come una persona al día.
# total_raciones: Cuántas raciones hay en el almacén en total.
# El programa debe calcular y mostrar:
# Cuántas raciones se consumen en un día en total.
# Para cuántos días exactos alcanza la comida.
# Si cada día se desperdicia un 10% de la comida por culpa de las ratas, ¿cuántas raciones se pierden al día?