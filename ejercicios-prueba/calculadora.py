# Crea un programa que:
# Pida al usuario dos números.
# Realice la suma, resta, potencia, multiplicación y división de esos números.
# Muestre los resultados en pantalla.
# Pregunta si desea realizar otra operacion si es asi repite el proceso de lo contario termina el proceso

def pregunta_operaciones(num1, num2):
    resultado = int(input("""Que operacion deseas realizar?
    -----------------------------------------
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Resto
    6. Potencia
    -----------------------------------------
    Elige una operacion: """))
    
    if resultado == 1:
        print(f"El resultado es: {num1 + num2}")
    elif resultado == 2:
        print(f"El resultado es: {num1 - num2}")
    elif resultado == 3:
        print(f"El resultado es: {num1 * num2}")
    elif resultado == 4:
        print(f"El resultado es: {num1 / num2 if num2 != 0 else 'Error división por cero'}")
    elif resultado == 5:
        print(f"El resultado es: {num1 % num2 if num2 != 0 else 'Error resto por cero'}")    
    elif resultado == 6:
        print(f"El resultado es: {num1 ** num2 if num2 != 0 else 'Error potencia por cero'}")     
    else:
        print("No existe la operacion")
        
    pregunta = input("Deseas realizar otra operacion? (s/n): ")
    
    if pregunta == "s":
        pregunta_operaciones(num1, num2)
    elif pregunta == "n":
        print("Proceso terminado")
        exit()
    else:
        print ("Error")
        
        
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
        
pregunta_operaciones(num1, num2)