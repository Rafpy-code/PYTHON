"""Creacion de una lista

even_numbers= []
for i in range(20):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)"""

import time
from datetime import datetime

#lista de la compra.
listaCompra = []
interruptor = True
finalizar = 'S'
    
print('Lista de la compra')

"""def compra():
    articulos = input('¿Qué necesitas comprar? ')
    listaCompra.append(articulos)
    #print(listaCompra)
    finalizar = input('¿<S> si deseas cerrar la lista de la compra?')
    if finalizar == 's' or finalizar == 'S':
        print(f'\nTu lista de la compra a fecha: {datetime.today()}')
        #print(datetime.today())
        print (listaCompra)
        interruptor = False
    return listaCompra"""

while interruptor:
    articulos = input('¿Qué necesitas comprar? ')
    listaCompra.append(articulos)
    #print(listaCompra)
    finalizar = input('¿<F> si deseas cerrar la lista de la compra?')
    if finalizar == 'f' or finalizar == 'F':
        #print(datetime.today())
        interruptor = False
        salir = input('¿Seguro deseas terminar? <S> ').upper()
        if finalizar == 's' or finalizar == 'S':
            interruptor = False
print(f'\nTu lista de la compra a fecha: {datetime.today()}')
print (listaCompra)
            
            
