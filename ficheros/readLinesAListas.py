newlista=[]
newlistaSinSaltos=[]
newLineas=[]
concatena=''

with open('readLinesAListas.txt') as f:
    for palabra in f:
        concatena += palabra.replace('\n', ' ')
        newlista.append(palabra)
        newlistaSinSaltos.append(palabra.replace('\n', ''))
print(f'Líneas concatenadas en una cadena de texto: {concatena}')
print(f'Línea añadida directamente a una lista: {newlista}')
print(f'Lista limpia con .replace(): {newlistaSinSaltos}')

with open('readLinesAListas.txt') as f:
    lineas= f.readlines()
print(f'Carga toda en una lista y  carga todo en memoria: {lineas}')

with open('readLinesAListas.txt') as f:
    otralista = [linea.rstrip() for linea in f]
    maplista = list(map(str.rstrip, f))
print(f'Lista limpia sin barra n con .rstrip(): {otralista}')
print(f'Lista list(map(str.rstrip())): {otralista}') 

"""
#Lista de enteros
lista = [int(linea) for linea in f]
lista = list(map(int, f)) 

#Lista de strings
lista = [linea.rstrip() for linea in f]
lista = list(map(str.rstrip, f))
"""
  