# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:35:26 2022 @author: Ramón
Crea  un  programa  que  permita  al  usuario  crear  un  poema,  
este  irá entrando  las líneas de  dicho  poema hasta  que  decida  
terminar  de hacerlo, en ese momento, el programa guardará todo el 
poema en un fichero de texto llamado “poema.txt”.
"""
#libreria para ficheros
from io import open

#Declaro las variables.
rutaMenu = 'ej1poemaMenu.txt'
rutaSalida = 'ej1poemaExit.txt'
interruptor = True
opcion = 'A'
frase = 'EXIT'
poema = []

#Defino las funciones.
def menu(ruta):
    with open(ruta) as f:
        lineas = f.read()
    print(f'{lineas}')
    return opcion

def crearPoema():
    if frase == 'EXIT':
        print('Tu poema')
        guardarPoema(poemaCreado)
        interruptor = False
    else:
        poema.append(frase)
    #print(poema)
    return poema

def guardarPoema(poemaCreado):
    for linea in poemaCreado:
        with open(rutaSalida, 'a') as f:
            f.write(f'{linea}\n')
            poema = []
    
    with open(rutaSalida) as f:
        for linea in poemaCreado:
            print(linea.capitalize())
        return linea

#LLamo a la función para leer del menu desde el archivo.
menu(rutaMenu)
opcion = input('Crear Poema?: ').upper()

while interruptor:
    
    #LLamo a la función para crear el poema.
    if opcion == 'C' :      
        frase = input('Escribe aquí tu inspiración: ').upper()
        poemaCreado = crearPoema()

    if frase == 'EXIT':
        interruptor = False
        menu(rutaMenu)
        opcion = input('Crear Nuevo Poema?: ').upper()
        