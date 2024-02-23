"""
Crear un diccionario mediante inputs
rae['enjuiciar'] = {'Someter una cuestión a examen, discusión y juicio'}"""

print('Creador de un diccionario')

diccionario = {}
contador = 0

while contador <= 3:
    clave = input('Ingresa la clave: ')

    valor = input('Ingresa el valor: ')

    diccionario[clave] = valor
    contador+=1
print(diccionario)
for clave,valor in diccionario.items():
    print(f'{clave}: {valor}')