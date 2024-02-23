def calculadora():
    operacion = input("¿Qué operación quieres hacer?Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")
    num1 = float(input("Introduce el primer valor: "))
    num2 = float(input("Introduce el segundo valor: "))
    if(operacion == "suma"):
        print(num1 + num2) 
    elif(operacion == "resta"):
        print(num1 - num2) 
    elif(operacion == "potencia"):
        print(num1**num2) 
    else:
        print("Operación errónea. Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")

print("Apartado 6: Ejercicio 2. Mini calculadora")
calculadora()