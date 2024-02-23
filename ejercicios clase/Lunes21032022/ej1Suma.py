"""
Crea un programaque pida números que irá sumando. “Pero”solo sumará aquellos números que sean menores a 10
Cuando el total de la suma lleguea 100, el programa terminará y mostrara la suma.
"""
print('Suma números menores de 10, al llegar a 100 se detiene.')
interruptor = True
total = 0
while interruptor:
    numero = int(input('Ingresa un número: '))
    if 0 < numero < 10:
        total = int(total +numero)
    else:
        print('Este número no se sumará')
    if total >= 100:
        interruptor = False
print (f' Hemos llegado al objetivo: {total}')