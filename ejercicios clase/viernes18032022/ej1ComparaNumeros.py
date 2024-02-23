"""
Crea un programa que pida un número por pantalla, este debe determinar si el número es mayor o menor
que un límite también pedido por pantalla, por lo tanto,el programa pide dos cosas, el numero a comparar,
y el límite al cual comparamos, luego tiene que mostrar un mensaje por pantalla que diga:
“el número es mayor” o “el número es menor”
"""

#Declaro las variables.
numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))

#Realizo las comparaciones e imprimo los resultados.
if(numero1 > numero2):
    print(f'\tEl número {numero1} es mayor que {numero2}.\n')
else:
        print(f'\tEl número {numero2} es mayor que {numero1}.\n')