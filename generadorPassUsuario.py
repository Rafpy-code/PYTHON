# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:42:17 2022 @author: Ramón
Generador de contraseñas a petición del ususario
"""
import string
import colorama
from colorama import Fore,Style,init,Back
#BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
import random
from random import choice,sample,shuffle
#SI DESEO ENCRIPTAR LA CONTRASEÑA.
#from werkzeug.security import generate_password_hash


#Declaro las variables.
grupoM = ''
grupom = ''
grupon = ''
grupos = ''
mix = ''
password = ''

#Estos datos los obtengo de la lib string.
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros    = string.digits
simbolos = string.punctuation

#Para darle color a los textos, recordar resetear al final.
print(f'{Fore.MAGENTA+Style.BRIGHT}{mayusculas}\n{minusculas}\n{numeros}\n{simbolos}{Style.RESET_ALL} ')

#Solicito al usuario que ingrese el valor para cada secuencia
print(f'\n{Back.RED}{Fore.WHITE}{Style.BRIGHT}GENERADOR DE CONTRASEÑA ESCOGIENDO LOS CARACTERES QUE SE SOLICITA\n{Style.RESET_ALL}')
M = int(input(f'{Fore.CYAN}{Style.BRIGHT}¿Cuántas MAYÚSCULAS necesitas? '))
m = int(input('¿Cuántas minúsculas necesitas? '))
n = int(input('¿Cuántas números necesitas? '))
s = int(input(f'¿Cuántos símbolos necesitas? {Style.RESET_ALL}'))

#Realizo mi metodo con parámetros
def passwordSegura(M,m,n,s):
    grupoM = sample(mayusculas,M)
    grupom = sample(minusculas,m)
    grupon = sample(numeros,n)
    grupos = sample(simbolos,s)
    #Uno todas las secuencias de caracteres.
    mix = grupoM + grupom + grupon + grupos
    #Mezclo la secuencia unnida.
    shuffle(mix)
    #Devuelvo el valor como una cadena de carácteres.
    password = ''.join(mix)  
    #retorno el valor generado.
    return print(f'\n{Fore.BLUE}{Style.BRIGHT}Tu contraseña es: {Fore.YELLOW}{Style.BRIGHT}{password}{Style.RESET_ALL}')

#Llamo a la función.
passwordSegura(M, m, n, s)