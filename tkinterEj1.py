# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:13:06 2022 @author: Ramón
import tkinter
ventana = tkinter.Tk()
ventana.mainloop()
Este codigo es el que nos muestra la ventana, y ya podemos añadir
todo lo que necesitemos.
"""
import tkinter
#Definir constantes para lo que se quiera usar en la ventana

#Se crea la ventana
ventana = tkinter.Tk()

#Con geometry('medidas')
ventana.geometry('400x300')

#Para mostrar un titulo tkinter.Label(ventana, text='el texto a mostrar') 
etiqueta = tkinter.Label(ventana, text='Ramón', font='Helvetica 20', bg='red', fg='white')
#dentro de pack(side=tkinter.RIGHT) podemos poner la posición del texto.
#pack(fill = tkinter.Y,expand=True) Y necesita el expand.
etiqueta.pack(fill = tkinter.X)

#Para hacer un cuadro de texto para recibir valores cajaTexto = tkinter.Entry(ventana).
cajaTexto = tkinter.Entry(ventana, font='Helvetica 20')
cajaTexto.pack()

#Hay que ir poniendo el codigo para luego ir mostrando en la ventana.
nombre = cajaTexto.get()
def saludo(nombre):
    print(f'Bienvnid@ {nombre} ')
'''
otraEtiqueta = tkinter.Label(ventana. text='aquí se imprime', fg='blue')
otraEtiqueta.pack()

bt_add = tkinter.Button(ventana, text = 'Presiona', command = textoDeLaCaja
bt_add.pack()

def textoDeLaCaja():
    frase = cajaTexto.get()
    otraEtiqueta['text'] = frase
'''
    
#Button para crear botones y dentro command para ejecutar, la funcion va sin paréntesis.
#Se pone padx y pady para darle medidas al botón
bt_add = tkinter.Button(ventana, text = 'Añadir artículo', command = lambda: saludo(nombre))
bt_add.pack()

ventana.mainloop()