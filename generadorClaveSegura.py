# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 14:07:15 2022 @author: Ramón
"""

import string
import random
from werkzeug.security import generate_password_hash

print("Generador de contraseñas seguras\n")
#abcedarioCompleto = string.ascii_letters
#print(abcedarioCompleto)
#espacios   = string.whitespace
minusculas = string.ascii_lowercase
print(minusculas)
mayusculas = string.ascii_uppercase
print(mayusculas)
numeros    = string.digits
print(numeros)
simbolos = string.punctuation
print(simbolos)
#todoJunto  = string.printable #Este no funciona REVISAR
#print (todoJunto)

#Mezclo todas las cadenas declaradas
mezcla = minusculas + mayusculas + numeros + simbolos

longitudPassword = int(input('¿Longitud del password? '))

#Se introduce la variable y la longitud de caracteres que se desee
mix = random.sample(mezcla, longitudPassword)

#Convertimos en una sola cadena de texto sin espacios "" el random.sample()
password = "".join(mix)

print(f'\nContraseña generada =>\t {password}')

#Aquí se encripta la contraseña con Hash256
passwordEncriptado = generate_password_hash(password)

print(f'\nContraseña encriptada =>\t {passwordEncriptado}')