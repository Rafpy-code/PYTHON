# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:07:40 2022 @author: Ramón
Crea un programa que analice un párrafo. Este debe ser recogido por 
un fichero llamado “párrafo.txt”. El programa analizara la cantidad 
de palabras que tiene. Luego el usuario, debe introducir un número, 
ese numero es la cantidad de palabras que el usuario determina como 
máximas. Si el párrafo tiene mas palabras que el número entrado por 
el usuario mandará un mensaje indicando que el numero es superior y 
también diciendo cuantas palabras sobran.
"""
from io import open
import string

#Declaro las variables.
rutaSalida = 'ej2salidaContPalabras.txt'
interruptor = True
frase = 'EXIT'
lineasPoema = 0
contadorPalabras = int(0)
poema = []
listaLimpia = []

print('Contador de palabras\n')
#Solicito al usuario que vaya introduciendo sus palabras
opcion = input('<exit> para salir\n<enter> para continuar ').upper()

while interruptor:
    frase = input('Escribe aquí tu inspiración: ').upper()
    poema.append(frase)
        
    if frase == 'EXIT':
        interruptor = 0
#Sobreescribo el archivo para que cada vez se renueve.       
with open(rutaSalida, 'w') as f:
    poema.pop()
    for lineas in poema:
        f.write(f'{lineas}\n')
    poema = []

totalPalabras = int(input('¿Cuántas palabras querías?\n'))
with open(rutaSalida) as f:
    for linea in f:
        for palabra in linea:
            contadorPalabras+=1

contador = contadorPalabras//2
#En la condición imprimo y cierro el interruptor.
if contador == totalPalabras:
    print('\nEste es tu poema\n')  
    with open(rutaSalida) as f:
        print(f.read().capitalize()) 
        print(f'Hay {contador} palabras. Haz acertado.')

elif contador < totalPalabras:
    print('\nEste es tu poema\n')  
    with open(rutaSalida) as f:
        print(f.read().capitalize())
        
        faltan = totalPalabras - contador
        print(f'Hay {contador} palabras. te faltan {faltan} palabras.')
else:
    print('\nEste es tu poema\n')  
    with open(rutaSalida) as f:
        print(f.read().capitalize())
        
        sobran = contador - totalPalabras
        print(f'Hay {contador} palabras. te has pasado {sobran} palabras.')