#creado una funcion simple 
print('----------------------------------------')

def saludar():
    print('Hola desde la funcion saludar')
    
saludar() #llamando la funcion
print('----------------------------------------')

#creando una funcion con parametros
def saludar_genero(nombre, sexo):
    if sexo == 'm':
        print(f'Hola {nombre}, eres genero masculino')
    elif sexo == 'f':
        print(f'Hola {nombre}, eres genero femenino')
    else:
        print(f'Hola {nombre}', 'No especificaste tu genero')
#llamando la funcion con parametros
saludar_genero('Juan', 'm')

# creando una funcion con parametros que pida a traves de un input
def desarrollador():
    tipo_desarrollador = input('''----------------------------------------
                               Si eres fronted Escribe una "f"
                               Si eres Backend escribe una "b"
                               Si eres FullStack entonces una "fs":''').lower()
    if tipo_desarrollador == "f":
        print('''Eres un desarrollador Frontend y deberias de aprender:
              -HTML
              -CSS
              -JavaScript
              Y Frameworks como:
              -React
              -Angular
              -Vue''')
    elif tipo_desarrollador == "b":
        print('''Eres un desarrollador Backend y deberias de aprender:
              -Python
              -Java
              -NodeJS
              -PHP
              Y Frameworks como:
              -Django
              -Spring
              -Express
              -Laravel''')
    elif tipo_desarrollador == "fs":
        print('''Eres un desarrollador FullStack y deberias de aprender:
              -HTML
              -CSS
              -JavaScript
              -Python
              -Java
              -NodeJS
              -PHP
              Y Frameworks como:
              -React
              -Angular
              -Vue
              -Django
              -Spring
              -Express
              -Laravel''')    
    else:
        print('No eres un desarrollador')
        
# desarrollador()

# crear una funcion que retorne un valor

def crear_contraseña_random(num):
    letras = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña= f"{letras[c1]}{letras[c2]}{letras[c3]}{num * 2}"
    return contraseña, num
    
password = crear_contraseña_random(489)
frase = f'Tu contraseña es: {password}'
print(frase)
