import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
#Se puede convertir a entero en el momento de recibir el valor.
n = int(input("Ingresa el número para calcular el factorial: "))
print(factorial(n))
"""
#Y se puede convertir a entero en el momento de imprimir el valor.
n = input("Ingresa el número para calcular el factorial: ")
print(factorial(int(n)))

borrarPantalla()