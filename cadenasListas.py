#Diferentes maneras de selecionar la posición de la cadena.
cadena = 'Ramón Francisco'
print (cadena[2])
print (cadena[2:])
print (cadena[2:5])
print (cadena[:5])
print (cadena[-5])
print (cadena[2:-5])
print (cadena[:-5])
#Crea una cadena nueva, ordenada según los valores ASCCI
ordenada = sorted(cadena)
print (ordenada)
ordenada1 = " ".join(sorted(cadena))
print (ordenada1)

#Ahora con  LISTAS de números funciona igual los print de arriba.
numeros = [500,23,496,39,124,18,290,987]
print (f'Esta es la lista original: {numeros}')

longitud = len(numeros)
print (f'longitud de la lista: {longitud}')

numeros.sort()
print (f'Esta es la lista ordenada {numeros}')

numerosOrdenados = sorted(numeros)
print (f'sorted() devuelve una nueva lista ordenada {numerosOrdenados}')

numeros.pop()
print (f'Pop() elimina el último valor de la lista {numeros}')

numeros.pop(3)
print (f'Pop(3) elimina la posición dada de la lista {numeros}')

numeros.insert(3, 1973)
print (f'insert(3, 1973) inserta un valor en la posición dada {numeros}')

numerosReves = sorted(numerosOrdenados, reverse = True)
print (f'Lista reversada {numerosReves}')