"""
Crea un programa donde establezcas una contraseña, esta contraseña será un string de 10.
El programa, luego, pedirá un nombre de usuario y una contraseña.
Crea mediante un bucle FOR un algoritmo que compare las dos cadenas y determine,
en caso de que la contraseña sea correcta, si puede ingresar o no el usuario al sistema.
"""
#Solicito al usuario que ingrese los datos para evaluar.
usuarioIng = input('Ingresa tu usuario: ')
passIng = input('Ingresa tu contraseña: ')
usuario = usuarioIng.upper()#Para pasar el nombre a mayúsculas.
#Declaro la variable para comparar con la introducida.
password = 'pericotetu'

#Realizo las comparaciones correspondientes e imprimo.
if password == passIng:
    print(f'\t\vBienvenido {usuario}.')
else:
        print(f'\t\vALERTA...USUARIO: {usuario}...desconocido!!!')