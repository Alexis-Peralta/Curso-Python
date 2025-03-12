diccionario = {
    "nombre": "Sergio",
    "apellido": "Pérez",
    "edad": 30
}

print('----------------------------------------')

for key in diccionario:
    print(f"{key}: {diccionario[key]}")
    
print('----------------------------------------')
    
    
#recorriendo diccionario con items() para obtener clave 

for key in diccionario:
    key
    print(f"la clave es {key}")
    
print('----------------------------------------')
    
    
#recorriendo diccionario con items() para obtener clave y valor

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"{key}: {value}")