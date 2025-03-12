# Se debe tomar en cuenta que unicamente funciona con numeros, no con strings

numeros = [1, 12, 25, 38, 49]

print('----------------------------------------')
numero_alto = max(numeros)
print(f'El numero mas alto es: {numero_alto}')

print('----------------------------------------')
numero_bajo = min(numeros)
print(f'El numero mas bajo es: {numero_bajo}')

print('----------------------------------------')
numero = round(3.1416)
print(f'El numero es "3.1416" y redondeado es: {numero}')

#retorna false cuando el valor es 0, vacio, falso o none
print('----------------------------------------')
valor = bool(0)
print(f'El valor es bool: {valor}')

#retorna true cuando todos los valores son verdaderos
print('----------------------------------------')
valor = all(numeros)
print(f'El valor es all: {valor}')

#sumar todos los valores iterables
print('----------------------------------------')
valor = sum(numeros)
print(f'El valor es sum: {valor}')