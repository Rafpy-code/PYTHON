numero1 = int(input('Ingresa el primer número'))
numero2 = int(input('Ingresa el segundo número'))

mediaAritmetica = int((numero1+numero2)/2)
opcion = 0

if mediaAritmetica > 0 and mediaAritmetica < 10:
    opcion = 1
elif mediaAritmetica >= 10 and mediaAritmetica < 50:
    opcion = 2
elif mediaAritmetica >= 50:
    opcion = 3
else:
    opcion = 4
    
match opcion:
    case 1:
        print('Nivel bajo de eficiencia')
    case 2:
        print('Nivel medio de eficiencia')
    case 3:
        print('Nivel alto de eficiencia')
    case 4:
        print('Valores inválidos')
