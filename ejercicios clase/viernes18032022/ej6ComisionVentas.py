"""
Vamos Queremos gestionar las comisiones de nuestra empresa, para asignar, a cada trabajador,
el % de comisión que merece teniendo en cuenta las ventas que ha realizado durante el mes.
Por lo tanto, el programa, pedirá el nombre del comercial y la cantidad vendida en el mes.
Después, dependiendo de la cantidad, se la dará la comisión correspondiente, teniendo en
cuenta, los siguientes rangos:
Menos de 10000 –“No tienes comisión” 0%
De 10000 a 30000 –“Comisión básica” 3% Mas
De 30000 –“Comisión máxima” 5% El programa deberá mostrar la siguiente linia:
Albert ventas: 30000 –Comisión asignada: Comisión máxima –1500 TOTAL 31500
Recuerda: 1. La comisión es las ventas * por la comisión / 1002. El total es Ventas + comisión
"""
#Declaro las variables ya como float para las operaciones que necesito.
comision0 = float(0.00)
comision1 = float(0.03)
comision2 = float(0.05)
ventas    = float(0.00)
obtiene   = float(0.00)
total     = float(0.00)
vendedor  = 'Ramón'
    
#Solicitamos que ingresen los datos, nombre y cantidad vendida.
vendedor = input("Ingrese el nombre del vendedor:\t\t")
ventas = int(input("Ingrese el total de las ventas realizadas:\t"))
    
#Realizo las condicionales e imprimo los resultados.
if (ventas > 0 and ventas < 10000):
    obtiene = comision0 * ventas
    total   = ventas + obtiene
    print(f" El vendedor: {vendedor} \n Ha vendido: {ventas} \n Obtiene una comisión de: {obtiene} \n TOTAL {total}")

elif ventas >= 10000 and ventas <= 30000:
    obtiene = comision1 * ventas
    total   = ventas + obtiene
    print(f" El vendedor: {vendedor} \n Ha vendido: {ventas} \n Obtiene una comisión de: {obtiene} \n TOTAL {total}")
        
elif ventas > 30000:
    obtiene = comision2 * ventas
    total   = ventas + obtiene
    print(f" El vendedor: {vendedor} \n Ha vendido: {ventas} \n Obtiene una comisión de: {obtiene} \n TOTAL {total}")

else:
    print("Has introducido un dato incorrecto")