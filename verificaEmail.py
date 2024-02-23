# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:51:13 2022 @author: Ramón
Programa para comprobar si un dirección de mail es correcta
"""
print("Comprobación de email:\n\
      ejemplo@empresa.dominio")

email = input("Digite la direccion de correo electronico: ")
valido = True
contadorArroba = 0
contadorPunto = 0
"""
#buscados: @ y .
for buscados in email:
    
    if(buscados == '@'):
        contadorArroba += 1
    posicionArroba = email.find('@')
    
    if(buscados == '.'):
        contadorPunto += 1
    posicionPunto = email.find('.')
        
if(contadorArroba == 1 and contadorPunto == 1 and posicionArroba > 0 and posicionPunto > 2):
    print(f"\nEl email: {email} es correcto!")
    print(f"El email contiene {contadorArroba} @ en la posición {posicionArroba}.")
    print(f"El email contiene {contadorPunto} '.' en la posición  {posicionPunto}.")
    #print(valido)
    
else:
    valido = False
    print(f"\n>>>Email con formato erroneo: {email}<<<");
    #print(valido)
"""
arroba = '@' in email           #devuelve True o False
arroba1 = email.count('@')      #Cuenta las coincidencias
posArroba = email.index('@') +1 #Devuelve la posición desde 0
punto = email.find('.')         #Devuelve la posición desde 0
posPunto = email.index('.') +1  #Devuelve la posición desde 0
reemplazar = email.replace('@', '$')

print(f'{arroba1}@ {arroba} posición {posArroba}\n"." {punto} posición {posPunto}')
print(reemplazar)