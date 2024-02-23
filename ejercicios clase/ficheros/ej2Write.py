ruta = 'dat/ej2Write.txt'
palabras = ('hola', 'Ramon', 'Francisco')

#Abre el fichero en modo escritura
f = open(ruta, 'w')
#Recorro la lista 
for palabra in palabras:
    f.write(palabra + '\n')
f.close()

#Ahora leo el contenido para ver si funciona el write.
f = open(ruta)
for linea in f:
    print(linea)
f.close()



#Ahora añado más contenido para ver si funciona el añadir 'a'.
palabras = ('Hasta', 'la', 'próxima', 'amigo')
f = open(ruta, 'a')
#Recorro la lista 
for palabra in palabras:
    f.write(palabra + '\n')
f.close()

#Recorro e imprimo el nuevo fichero.
f = open(ruta)
for linea in f:
    print(linea)
f.close()