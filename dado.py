import random
#Tirada de dado, o también para adivinar el número
dado = random.randint(1, 6)
#print (dado)

#Se puede usar un for y realizar 2 tiradas de dados o más y así sacar 1 número de media.
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

dado = (dado1 + dado2)//2
print(f"(dado1 {dado1} + dado2 {dado2}) //2")
print (dado)