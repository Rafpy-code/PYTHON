# -*- coding: utf-8 print(0xe838)-*-
"""
Created on Fri Apr  1 18:38:36 2022 @author: Ramón
Crea  un  programa  que recoja  los  datos  de  un  fichero  
(ver  ejemplo) donde se guardan parejas de valores, el programa tiene 
que separar los valores de la primera fila y llamarlos valores1 y los 
de la segunda fila y llamarlos valores 2. 
Recomendación: Trabaja dichos valores en el mismo momento que cojes 
una línea. Una vez realizada la tarea de importación, el programa 
hará una exportación donde creara dos ficheros de texto, 1 para los 
valores1 y otro para los valores2
"""
from io import open

valores1 = []
valores2 = []
longitud = 0
i = 0

#Primera lectura para saber las líneas del archivo.
with open('ej4dosValores.txt') as f:
    #Con el sum sumo cada iteración del for en cada línea del archivo.
    totalLineas = sum(1 for linea in f)
    print(f'El fichero tiene {totalLineas} lineas en total.')

    
with open('ej4dosValores.txt') as f:
    #La función map devuelve un iterable, rstrip elimina las barra n.
    listaSeparadas = list(map(str.rstrip, f))
    #print(listaSeparadas)
    
    while i < totalLineas:
        #print(listaSeparadas[i])      
        #split donde encuentre un espacio lo separa por coma
        columna = listaSeparadas[i].split(' ')
        print(columna)
        
        #Voy añadiendo los valores de cada columna en una lista separada.
        valores1.append(columna[0])
        valores2.append(columna[1])
        #Incremento mi contador
        i += 1  
    
    #Imprimo los valores de las listas obtenidas.
    print(f'Valores de la columna 1: {valores1}')
    print(f'Valores de la columna 2 {valores2}')

print('\nArchivo: ej4Valores1.txt')
with open('ej4Valores1.txt', 'a') as f:
    for valor in valores1:
        f.write(f'{valor}\n')
        print(valor)
    
print('\nArchivo: ej4Valores2.txt')
with open('ej4Valores2.txt', 'a') as f:
    for valor in valores2:
        f.write(f'{valor}\n')
        print(valor)