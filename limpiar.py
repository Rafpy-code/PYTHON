"""
import platform
import os
import time

def limpiarPantalla():
    time.sleep(3)
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('cleaar')
        
if __name__ == "__main__":
    limpiarPantalla()
"""
opcion = 1   
match opcion:
    case 1: print('lo logramos')