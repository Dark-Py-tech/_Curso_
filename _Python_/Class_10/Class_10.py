# def fib(n, profundidad=0):
#     # Creamos un prefijo con tabulaciones según la profundidad actual
#     tabulaciones = "\t" * profundidad
    
#     # Imprimimos la entrada a la función
#     print(f"{tabulaciones}➜ Entrando a fib({n})")

#     if n < 1:
#         print(f"{tabulaciones}⇠ fib({n}) devuelve None")
#         return None
#     if n < 3:
#         print(f"{tabulaciones}⇠ fib({n}) devuelve 1")
#         return 1
    
#     # Avisamos que vamos a calcular la suma de los dos hijos
#     print(f"{tabulaciones}  Calculando: fib({n-1}) + fib({n-2})")
# # Llamadas recursivas aumentando la profundidad
#     resultado_izq = fib(n - 1, profundidad + 1)
#     resultado_der = fib(n - 2, profundidad + 1)
    
#     resultado_total = resultado_izq + resultado_der
    
#     # Imprimimos el resultado antes de salir de este nivel
#     print(f"{tabulaciones}⇠ fib({n}) devuelve {resultado_total} (de sumar {resultado_izq} + {resultado_der})")
#     return resultado_total

# print("--- INICIO DE LA EJECUCIÓN ---")
# resultado_final = fib(5)
# print("------------------------------")
# print("Resultado final:", resultado_final)


# Tuplas 

# mutablemente inmutables

# nombre = "césar"            # inmutable
# apellido = "martin"         # inmutable
# lista = [2000, 3000, 4000]  # mutable

# tupla = (nombre, apellido, lista)   # empaquetadod e tupla

# nom, ape = tupla[:2]                # desempaquetado de tupla


# print(nom)
# print(ape)


#Dictionary

# class Empleado:
#     def __init__(self, nombre, apellido, salario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.salario = salario

#     def mostrar_info(self):
#         print(f"Nombre: {self.nombre}")
#         print(f"Apellido: {self.apellido}")
#         print(f"Salario: {self.salario}")

#     def __hash__(self):
#         return hash((self.nombre, self.apellido, self.salario))

#     def __eq__(self, other):
#         if not isinstance(other, Empleado):
#             return NotImplemented
#         return (
#             self.nombre == other.nombre and
#             self.apellido == other.apellido and
#             self.salario == other.salario
#         )

# emp1 = Empleado("César", "Martín", 2345)
# emp2 = Empleado("César", "Martín", 2345)

# print(id(emp1))

# print(id(emp2))


# print(f"El Hash de emp1 es: {hash(emp1)}")

# print(f"El Hash de emp2 es: {hash(emp2)}")


# print(-6517238952872247409 % 8)

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# # keys() proporciona acceso a la lista de claves
# print(".keys()")
# for clave in dictionary.keys():
#     print("\t" + clave, "->", dictionary[clave])

# # values() devuelve una lista de los valores
# print(".values()")
# for valor in dictionary.values():
#     print("\t" + valor)
    
# # .items() devuelve tuplas de clave y valor
# print(".items()")
# for tupla in dictionary.items():
#     print("Clave:", tupla[0], "- Valor:", tupla[1])

# # mucho más cómodo con el desempaquetado de tuplas
# for (clave, valor) in dictionary.items():
#     print("Clave:", clave, "- Valor:", valor)

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# # keys() proporciona acceso a la lista de claves
# print(".keys()")
# for clave in dictionary.keys():
#     print("\t" + clave, "->", dictionary[clave])

# # values() devuelve una lista de los valores
# print(".values()")
# for valor in dictionary.values():
#     print("\t" + valor)
    
# # .items() devuelve tuplas de clave y valor
# print(".items()")
# for tupla in dictionary.items():
#     print("Clave:", tupla[0], "- Valor:", tupla[1])

# # mucho más cómodo con el desempaquetado de tuplas
# for (clave, valor) in dictionary.items():
#     print("Clave:", clave, "- Valor:", valor)
    
# #########################################################################    
# # añadir valor asociado a clave que no existe
# dictionary['pájaro'] = 'bird'
# print(dictionary)
# # reemplazar clave ya existente
# dictionary["pájaro"] = 'oiseau'
# print(dictionary)

# # también podemos añadir o actualizar con el método .update()
# dictionary.update({"pato": "canard"})
# print(dictionary)

# # eliminar claves con el comando del
# del dictionary['perro']
# print(dictionary)

# # también podemos eliminar el último elemento con .popitem()
# entrada = dictionary.popitem()

# print(entrada, " se ha eliminado del diccionario")
# print(dictionary)

# # y podemos volver a añadirlo al diccionario
# clave, valor = entrada
# dictionary[clave] = valor
# print(dictionary)


# # ordenación de claves y reversed para invertir el orden
# for clave in reversed(sorted(dictionary.keys())):
#     print("\t" + clave, "->", dictionary[clave])

# # ordenación de claves
# for clave in sorted(dictionary.keys()):
#     print("\t" + clave, "->", dictionary[clave])


# #Con tuplas

# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


# Con lista

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name].append(score) 
    else:
        school_class[name] = [score]
        
##############################################       
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)