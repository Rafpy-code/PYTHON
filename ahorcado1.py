# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:56:38 2022 @author: Ramón
Juego del ahorcado
"""
#Importo las librerías que necesito
import random
import time

#Declaro las variables según voy necesitando.
intentos = 10
letrasEncontradas = ''

#Declaro la lista de palabras a adivinar.
palabras = ['perro','gallina', 'gato', 'raton', 
            'pato', 'conejo', 'caballo', 'burro', 
            'canguro', 'delfin', 'tortuga']

#Creo una función para sacar una palabra aleatoria.
def escogerPalabra():
    return random.choice(palabras)
#print(escogerPalabra())

#Creo una función para iniciar el juego
def jugar():
    palabra = escogerPalabra()
    print(palabra)
    while True:
        buscada = ingresaLetras(palabra)
        if procesoBusqueda(buscada, palabra):
            print('Bien hecho, has ganado!!!')
            break
        if intentos == 0:
            print('Lo siento, no lo has conseguido!!!')
            print(f'La palabra era: {palabra}')
            break
#Funciones para el caso de que falle todo y se quede sin intentos          
def ingresaLetras(palabra):
    imprimirVacio(palabra)
    print(f'Intentos restantes: {intentos}')
    buscada = input('Introduzca una letra: ')
    return buscada

def procesoBusqueda(buscada, palabra):
    global letrasEncontradas
    global intentos
    intentos = intentos - 1 
    letrasEncontradas = letrasEncontradas + buscada
    return False

def imprimirVacio(palabra):
    mostrarLetras = ''
    for letra in palabra:
        if letrasEncontradas.find(letra) > -1:
            mostrarLetras = mostrarLetras + letra
        else:
            mostrarLetras = mostrarLetras + '-'
    print (mostrarLetras)
jugar()         