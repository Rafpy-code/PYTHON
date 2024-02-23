'''
Trabajando con ficheros guardados en la carpeta que contiene dat/ejercicio1leer.txt 
'''
#Esto imprime el contenido como un string.
f = open('dat/ejercicio1leer.txt')
print('f.read() lee todo como string ' + f.read())

#Esto imprime el contenido como una lista [].
f = open('dat/ejercicio1leer.txt')
print('f.readlines() hace una lista con los datos')
print(f.readlines())
print('\n')

#Esto imprime el recorrido de el archivo.
f = open('dat/ejercicio1leer.txt')
for linea in f:
   print (f'Con el for {linea}')
   
#Operaciones: suma con datos del archivo.
total = 0
f = open('dat/ejercicio1leer.txt')
for linea in f:
    total = total + int(linea)
print (f'Total de la suma = {total}\n')

#Operaciones: promedio con datos del archivo.
total = 0
contador = 0
promedio = 0
f = open('dat/ejercicio1leer.txt')
for linea in f:
    total = total + int(linea)
    contador+=1
    promedio = total/contador
print (f'Total = {total} \nFilas = {contador} \nPromedio = {promedio}')

#Operaciones: promedio con datos del archivo sin contar los ceros.
total = 0
contador = 0
promedio = 0
f = open('dat/ejercicio1leer.txt')

for linea in f:
    total = total + int(linea)
    
    #Sólo si el número de la línea es mayor a 0, sumo el contador
    if int(linea) > 0: 
        contador+=1
#print (contador)  
promedio = total/contador
print (f'Total = {total} \nFilas = {contador} \nPromedio sin valores 0 = {promedio}\n')

#Meter los datos en una lista
array = []

f = open('dat/ejercicio1leer.txt')
for linea in f:
    #Debemos pasar el int(linea) para que no salgan los \n del string
    array.append(int(linea))
    
print (f'array = {array}')
