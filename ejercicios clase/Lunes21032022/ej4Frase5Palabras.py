"""
Escribe un programa que, mediante la entrada de palabras, forme una frase,
utiliza la función correspondiente que encontraras en la carpeta “ejemplos de clase”
concretamente “sfuncinestrininglude.c” el programa terminará cuando hayamos
entrado 5 palabras como máximo.
"""
print('Programa que pida por consola 5 palabras y forme una frase')

#Declaro las variables.
interruptor = True
contador = 0
frase = ''
palabra = ''

#Pongo el while para iniciar y finalizar con interruptores.
while interruptor:
    if contador <= 5:
        palabra = input('Ingresa una palabra: ')
        #Voy concatenando las palabras entradas.
        frase = frase + palabra + ' ' 
        contador+=1
    #En la condición imprimo y cierro el interruptor.
    if contador == 5:
        print(f'La frase es: {frase}')
        interruptor = False

