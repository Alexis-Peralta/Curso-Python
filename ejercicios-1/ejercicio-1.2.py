frase = input("Introduce una frase y te dire cuanto tiempo te llevará decirla: ")

palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)

print("-----------------------------------------")
print(f"Dijiste {cantidad_palabras} palabras en {cantidad_palabras / 2} segundos")
print("-----------------------------------------")
print(f"Dalto lo dirian en {cantidad_palabras * 100 // 2 * 1.3 / 100} segundos")
print("-----------------------------------------")

if cantidad_palabras >= 120:
    print("Tienes mucho que decir")
    