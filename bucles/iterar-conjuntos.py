animales = {'gato', 'perro', 'serpiente'}
numeros = {1, 2, 3}

print('----------------------------------------')

#Recorrer la conjunto de animales

for animal in animales:
    print(animal)

print('----------------------------------------')

#Recorrer la conjunto de numeros y multiplicarlos por 10

for numero in numeros:
    print(numero*10)
    
print('----------------------------------------')

#Recorrer la conjunto de numeros y animales

for numero, animal in zip(numeros, animales):
    print(numero, animal)
    
print('----------------------------------------')

#Recorrer la conjunto de manera con correcta con su indice

# for num in range(2, 5):
#     print(num)

# for num in range(len(numeros)):
#     print(numeros[num])
    
# print('----------------------------------------')
    
#Recorrer la conjunto de manera con correcta con su indice

# for num in enumerate(numeros):
#     print(type(num))

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Indice: {indice} - Valor: {valor}")
    
print('----------------------------------------')

#usando el for/else

for numero in numeros:
    print(numero)
else:
    print('No hay mas numeros')