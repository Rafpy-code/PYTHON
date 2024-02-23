"""
Crea un programa que pida un número. Luego crea un bucle en el cual se pida otro numero
y una letra. Si la letra es una S el programa sumara, si la letra es una R el programa
restará es segundo valor. Terminará de pedir números y hacer cálculos si ponemos
una F de finalización.
"""
print('Programa para sumar, restar números hasta presionar <f>')

#Declaro las variables.
interruptor = True
numero1 = int(0)
numero = int(0)
total = int (0)
operacion = 'A'
suma = int(0)
resta = int(0)

valorInicial = int(input('Ingresa el valor inicial: '))
#Valor inicial para realizar las operaciones.
total = valorInicial

while interruptor:
    numero = int(input('Ingresa un número: '))
    operacion = str(input('Sumar <S>, Restar <R>, Finalizar <F>: ')).upper()
    
    #Realizo un match para hacer las operaciones.
    match operacion:
        case 'S':
            total = total + numero
            print(f'La suma es: {total}')
        case 'R':
            total = total - numero
            print(f'La resta es: {total}')
        case 'F':
            print(total)
            interruptor = False    