"""
Crea un programa que muestre una cuenta atrás desde 10
y que al final muestre un mensaje que diga “ignición”.
"""
import time

contador = 10
interruptor = True

while interruptor:
    while 0 <= contador <= 10:
        print(contador)
        time.sleep(1)   
        if contador == 0:
            print('\a \U0001f680 Ignición!!! \U0001f6f8' )
        interruptor = False
        contador-=1