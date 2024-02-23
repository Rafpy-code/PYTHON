num1 = int(input(' Primer número: '))
num2 = int(input('Segundo número: '))
num3 = int(input(' Tercer número: '))

if num1 > num2 and num1 > num3:
    if  num2 > num3:
        print(f'\t    num1 {num1} es el mayor,\n\
            num2 {num2} es el medio,\n\
            num3 {num3} es el menor.\n')
    else:
        print(f'\t    num1 {num1} es el mayor,\n\
            num3 {num3} es el medio,\n\
            num2 {num2} es el menor.\n')
        
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f'\t    num2 {num2} es el mayor,\n\
            num1 {num1} es el medio,\n\
            num3 {num3} es el menor.\n')
    else:
        print(f'\t    num2 {num2} es el mayor,\n\
            num3 {num3} es el medio,\n\
            num1 {num1} es el menor.\n')
        
if num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f'\t    num3 {num3} es el mayor,\n\
            num1 {num1} es el medio,\n\
            num2 {num2} es el menor.\n')
    else:
        print(f'\t    num3 {num3} es el mayor,\n\
            num2 {num2} es el medio,\n\
            num1 {num1} es el menor.\n')
"""
secuencias a comprobar
    123
    132
    231
    213
    312
    321
"""
    
    
