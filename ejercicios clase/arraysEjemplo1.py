datos = []
for i in range(1,6):
    nuevoDato = int( input( "Dime el dato número {}: ".format(i) ))
    datos.append(nuevoDato)

print ("\nArray original\n")
for i in range(1,6):
    print ( datos[i-1] )
print(datos)
    
print ("\nLos datos al reves son:\n")
for i in range(5,0,-1):
    print ( datos[i-1] )
