"""
Crea un programa que pida un número. Luego crea un bucle en el cual se pida otro numero
y una letra. Si la letra es una S el programa sumara, si la letra es una R el programa
restará es segundo valor. Terminará de pedir números y hacer cálculos si ponemos
una F de finalización.
"""
print('Programa para sumar números mientras <s> parará con <n>')

#Declaro las variables.
interruptor = True
numero1 = int(0)
numero = int(0)
total = int (0)
operacion = ''
suma = int(0)
resta = int(0)

while interruptor:
    numero = input('Ingresa un número: ')
    opercion = input('Sumar <S>, Restar <R>, Finalizar <F>: ')
    #operacion = operacion.upper()
    match operacion:
        case 'S':
            suma = suma + numero
            print(f'La suma es: {suma}')
        case 'R':
            resta = resta + numero
            print(f'La suma es: {resta}')
        case 'F':
            interruptor = False    
