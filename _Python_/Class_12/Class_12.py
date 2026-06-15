# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
# #################################################
# stack_object = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())
# #################################################
# stack_object2 = Stack()

# stack_object2.push("tres")
# stack_object2.push("dos")
# stack_object2.push("uno")

# print(stack_object2.pop())
# print(stack_object2.pop())
# print(stack_object2.pop())

# César Martín (INSTRUCTOR) 19:59
# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
# #################################################

# pila1 = Stack()
# pila2 = Stack()
# pila3 = Stack()

# pila1.push(1)                   # añade 1 en pila1
# pila2.push(pila1.pop() + 1)     # elimina el valor 1 de pila y añade el valor 2 (sumando 1) a la pila2
# pila3.push(pila2.pop() - 2)     # elimina el valor de de pila2 y añade el valor cero (restando 2) a pila3

# print(pila3.pop())



# Reutilizacion de codigo con variasmetodos

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
# #################################################
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def push(self, val):

#         self.__sum += val

#         Stack.push(self, val)           # reutilizando el código del método en la superclase

#     def pop(self):

#         val = Stack.pop(self)           # reutilizando el código del método en la superclase
#         self.__sum -= val
#         return val

#     def get_sum(self):
#         return self.__sum
# #################################################
# stack_object = AddingStack()

# for i in range(5):
#     stack_object.push(i)

# print(stack_object.get_sum())

# for i in range(5):
#     print("Retirado el valor " + str(stack_object.pop()))

#     print("Suma: " + str(stack_object.get_sum()))




# class ExampleClass:
#     def __init__(self, val=1):
#         self.first = val                # la norma!!!

#     def set_second(self, val):
#         self.second = val               # tampoco es una buena idea
# ########################################
# example_object_1 = ExampleClass()

# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5              # muy mala idea!!!

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)