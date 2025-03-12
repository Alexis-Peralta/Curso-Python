frutas = ['manzana', 'pera', 'mango']
cadena = 'Hola Mundo'
numeros = [2, 5, 8, 10]

print('----------------------------------------')

#evitando la pera

for fruta in frutas:
    if fruta == 'pera':
        continue
    print('Fruta:', fruta)
    
#evitar que siga ejecutando el bucle (si se coloca el else no se ejecutara despues del break)

print('----------------------------------------')

for fruta in frutas:
    if fruta == 'pera':
        break
    print('Fruta:', fruta)
    
#recorriendo la cadena de texto
    
print('----------------------------------------')
    
for letra in cadena:
    print(letra)
    
# for en una sola linea de codigo

print('----------------------------------------')

# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)
    
#     print(numeros_duplicados)

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)