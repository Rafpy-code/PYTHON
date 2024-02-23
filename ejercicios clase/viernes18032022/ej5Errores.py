"""
Debemos monitorizar una serie de servicios para controlar que no se bloquean
y que esta todo funcionando correctamente, para poder llevarlo a cabo de una
manera rápida y eficiente, queremos gestionar las alertas y controlar, mediante
un programa, que estado tiene en ese momento. Los valores son enteros y corresponden
a los siguiente:
101 –Error de proceso leve: Bloqueado por falta de recursos
103 –Error de proceso leve: El proceso a terminado con algunos errores
204 –Error grabe: No se ha podido ejecutar el proceso
404 –Error critico: El proceso provoca que otros colapsen
El programa debe pedir el nombre del proceso y mostrar un mensaje donde aparezca dicho nombre,
y la explicación del error “Alerta detectada:
el servicio [ nombre del proceso] produce el error [número del error]
–DETALLE: El mensaje de error correspondiente
”Alerta detectada: el servicio [teams] produce el error [404]
–Detalle: Error critico: El proceso provoca que otros colapsen
"""
#Declaro las variables.
error = 0;
    
#Declaro las variables de los servicios
noError  = "Ok"
error1   = "Ratón\t"
error2   = "Teclado\t"
error3   = "Pantalla\t"
error4   = "Ram\t"
    
#Declaro las variables para los textos
ok      = "¡¡¡TODO FUNCIONA CORRECTAMENTE!!!"
raton   = "101–Error de proceso leve: Bloqueado por falta de recursos-"
teclado = "103-Error de proceso leve: El proceso a terminado con algunos errores-"
pantalla= "204–Error grabe: No se ha podido ejecutar el proceso-"
ram     = "404–Error crítico: El proceso provoca que otros colapsen-"

#Imprimo los errores y solicitar al usuario que ingrese los datos.
print ("Errores posibles: \n 10 No hay errores \n 101 \n 103 \n 204 \n 404. \n")
error = int(input("Ingrese el código que le muestra la pantalla: \t"))

#Manejo los datos recibidos de error con SWITCH CASE y los imprimos.
match error: 
    case  10:
        print(f"\t Servicio: {noError}{ok}\n")
    case 101:
        print(f"\t Servicio: {error1}{raton}\n")
    case 103:
        print(f"\t Servicio: {error2}{teclado}\n")
    case 204:
        print(f"\t Servicio: {error3}{pantalla}\n")
    case 404:
        print(f"\t Servicio: {error4}{ram}\n")