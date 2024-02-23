#Para recorrer strings, listas, etc...

word = 'Python'
for letter in word:
    print(letter)

print('\n')

word = 'Python'
for i , j in enumerate(word):
    print(i , j)

print('\n')
    
for i in range(len(word)):
    print(i, word[i])
