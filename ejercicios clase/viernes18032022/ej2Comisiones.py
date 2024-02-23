"""
Realiza un programa atendiendo a las siguientes especificaciones. El usuario introducirá un capital,
este será un número entero. Si el capital introducido es superior a 10000, le aplicaremos una comisión
del 5%, esto se hace multiplicando el capital, por este valor.Capital * 5% Recuerda que este valor tiene
que ir asignado a una variable int también, aparte de hacer el cálculo debemos mostrar el texto
“Tu comisión es: “ y posteriormente mostrar esa comisión. Por lo contrario, si el capital no es superior
a 10000, debemos mostrar un mensaje por pantalla que indique “No has conseguido la comisión”.
"""
#Declaro las variables
comision  = float(0.05);
capital   = float(0.00);
obtiene   = float(0.00);
total     = float(0.00);
    
#Solicitamos que ingresen los datos.
capital = float(input(" Ingrese el capital:\t"))
    
#Realizo las condicionales*/
if capital > 10000:
    obtiene = comision * capital
    #Para ajustar el número de decimales round(variable, numero de decimales).
    obtiene = round(obtiene, 2)
    total   = capital + obtiene
    print(f" Ha ingresado: {capital}\n Obtiene una comisión de: {obtiene}%\n TOTAL: {total}")     
else:
    print("No llegas al monto para obtener una comisión") 