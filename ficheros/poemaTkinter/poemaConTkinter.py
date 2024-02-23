# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:05:06 2022 @author: Ramón
"""

#libreria para ficheros
from io import open
import tkinter
from tkinter import ttk

#Creo la ventana roota, dimensiones y título.
root=tkinter.Tk()
root.geometry('500x500')
root.title('Poema Gatuno')
#Para poner un color de fondo en la ventana principal
#root.configure(bg='beige')

#Se carga la imagen y se la mete en una Label para mostrarla.
logo = tkinter.PhotoImage(file="gatito.png")
lbl_logo = tkinter.Label(root, image=logo)
lbl_logo.pack(side='right')

lbl_entrada = tkinter.Label(root, text='Ingresa aquí tus frases')
lbl_entrada.place(x=50, y=20)
lbl_entrada.pack()


entrada_frases = ttk.Entry()
entrada_frases.place(x=50, y=50)

# Define un botón en la parte inferior de la ventana
btn_salida = tkinter.Button(root,fg='yellow',bg='black', text='SALIR Y CERRAR EL PROGRAMA', command=root.quit)
btn_salida.pack(padx=20, pady=20,side='left')

root.mainloop()     
'''
#Declaro las variables.
rutaMenu = 'poemaMenu.txt'
rutaSalida = 'poemaSalida.txt'
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
 '''  