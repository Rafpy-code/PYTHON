# -*- coding: utf-8 -*-
"""
Para pip o pip3
pip install colorama
pip3 install colorama //if you're using python3
Para anaconda
conda install -c anaconda colorama
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
Style. DIM, NORMAL, BRIGHT, RESET_ALL

import colorama
from colorama import Fore
from colorama import Style

colorama.init()
print(Fore.YELLOW + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT +  "This is the color of grass" + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT +  "This is a dimmer version of the sky" + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "This is the color of the sun" + Style.RESET_ALL)
print(Fore.WHITE + Style.BRIGHT + "This is the color of the moon" + Style.RESET_ALL)
"""
#Otra forma de colorear el texto.
from colorama import init, Fore, Style, Back

# Para iniciar colorama
init()

print("Texto color original")

print(Fore.YELLOW + Style.BRIGHT +"Texto color amarillo"+ Fore.MAGENTA + Style.BRIGHT +"Texto color magenta")
print(Fore.GREEN + "Texto color verde")
print(Fore.RED + "Texto color rojo")
print(Fore.BLUE + Back.YELLOW +"Texto color azul y fondo amarillo")

"""
print('\x1b[Modo de visualización; color de primer plano; color de fondo m + "contenido de salida" +\x1b[0m')
print('\x1b[0;30;41m '+ 'Hello world' + '\x1b[0m ')
print('\x1b[5;30;42m '+ 'Hello world' + '\x1b[0m ')
"""

from time import sleep
from colorama import Cursor, init
init()
print("Recursos Python")
sleep(3)
print(Cursor.BACK(15) + Cursor.UP(1) + "Ramón")