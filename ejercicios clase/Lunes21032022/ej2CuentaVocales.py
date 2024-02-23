"""
Crea un programa medianteuna frase que introducimos nos cuente, cuantas vocales hay de cada.
El programa tambiéntiene que contar las palabras que tiene y la longitud total de la frase
mostrando esa información al final.
"""
print('Programa que cuenta las vocales que hay en una frase')
interruptor = True
a = int(0)
e = int(0)
i = int(0)
o = int(0)
u = int(0)

while interruptor:
    frase = input('Ingresa la frase a analizar: ')
    for letra in frase:
        if letra.lower() in "a":
            a+=1
        elif letra.lower() in "e":
            e+=1
        elif letra.lower() in "i":
            i+=1
        elif letra.lower() in "o":
            o+=1
        elif letra.lower() in "u":
            u+=1
    if a==0 and e==0 and i==0 and o==0 and u==0:
        print('\tNo hay vocales')
        interruptor = False
    else:    
        print(f'Se encuentran:\nLa <a> {a} veces.\nLa <e> {e} veces.\nLa <i> {i} veces.\nLa <o> {o} veces.\nLa <u> {u} veces.')
        interruptor = False