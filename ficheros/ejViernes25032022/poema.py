# -*- coding: utf-8 -*-
"""Created on Sat Mar 26 12:30:41 2022 @author: Ramón
Utiliza un programa que, entre frases por consola, estas frases forman 
parte deun poema. El usuario, cuando ya no quiera escribirmas frases, 
tendrá la opciónde guardar el poema. Luego, el programa, le dirá al 
usuario, cuantas palabras y cuantas líneas tiene dicho poema para saber 
si se ha pasado o no.
"""

#Declaro las variables.
interruptor = True
contador = 0
lineasPoema = 0
frase = ''
poema = []
ruta = 'poema.txt'

lineasPoema = int(input('¿De cuantas frases deseas crear tu poema?\n'))

#Pongo el while para iniciar y finalizar con interruptores.
while interruptor:
    #Voy añadiendo las frases introducidas a la lista poema.
    if contador <= lineasPoema:
        frase = input('Ingresa una frase para tu poema: ')
        poema.append(frase)
        contador+=1
        
    #Abre el fichero en modo escritura
    f = open(ruta, 'w')
    #Recorro la lista 
    for linea in poema:
        f.write(linea + '\n')
    f.close()
        
    #En la condición imprimo y cierro el interruptor.
    if contador == lineasPoema:
        print('\nEste es tu poema\n')
        f = open(ruta)
        #for linea in f:
        #   print(linea)
        print(f.read().capitalize())
        f.close()
        interruptor = False