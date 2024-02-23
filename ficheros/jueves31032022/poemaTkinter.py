# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:36:24 2022 @author: Ramón
"""
#Hay que importar de la librería 'io' para que se creen los archivos, si estos no existen
from io import open
'''
#Escribo la ruta que deseo crear o abrir
with open('poemaTkinter1.txt','a',encoding="utf-8") as f:
    for num in range(0,10):
        f.write(f'{str(num)}\n')
'''    
with open('poemaTkinter1.txt') as f: 
    salida = f.readlines()
    print(salida)

with open('poemaTkinter1.txt') as f: 
    salida = f.readlines()
    num1 = int(salida[2])
    num2 = int(salida[6])
    suma = num1 + num2
    print(f'{num1} + {num2} = {suma}')
    