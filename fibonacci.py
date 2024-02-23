from math import*
#Calcula la suma de los nùmeros de la secuencia que se ingresa
def fibonacci(n):
     
    if n==0 or n==1:
        return n
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)
        return resultado

#n = input("Ingresa n para el fibonacci: ") 
#n = int(n) 
#print(fibonacci(n))

#Esto se ingresa el máximo de la secuencia que se desea ver
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

#n = input("Ingresa el maximo para el fibonacci: ") 
#n = int(n)     
#fib(n)

#Usando for para la secuencia fibonacci
n = input("Ingresa el maximo para el fibonacci: ") 
n = int(n)  
a, b = 0,1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
    fibonacci(n)
print(fibonacci(n))


