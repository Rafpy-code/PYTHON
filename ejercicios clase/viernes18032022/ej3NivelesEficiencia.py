"""
#print("Mi{:.2f} y {:.2f}".format(num1, num2)) para 2 decimales.
Crea un programa que pida 2 números por consola. Luego deberá hacer la media aritmética de estos
dos números y mostrar el resultado con 2 decimales. El programa, además, debe indicar que,
si el número está entre 0 i 10 mostrar un mensaje de “Nivel bajo de eficiencia”
si esta entre 10 –50 mostrará “Nivel medio de eficiencia” y
si esta por encima de 50 “Nivel óptimode eficiencia”. Utiliza el IF con ELIF par evaluar los
posibles casos y el MATCH CASE para mostrar los PRINT
"""
#Declaro las variables.
numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))

#Realizo las operaciones correspondientes.
mediaAritmetica = int((numero1+numero2)/2)
opcion = 0

#Realizo las comparaciones correspondientes.
if mediaAritmetica > 0 and mediaAritmetica < 10:
    opcion = 1
elif mediaAritmetica >= 10 and mediaAritmetica < 50:
    opcion = 2
elif mediaAritmetica >= 50:
    opcion = 3
else:
    opcion = 4
#Aquí realizo la impresión según el valor recibido de los if.    
match opcion:
    case 1:
        print('Nivel bajo de eficiencia')
    case 2:
        print('Nivel medio de eficiencia')
    case 3:
        print('Nivel alto de eficiencia')
    case 4:
        print('Valores inválidos')