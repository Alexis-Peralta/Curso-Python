lista = list(["hola", "mundo", 23]) #crea una lista

resultado = len(lista) #devuelve la longitud de la lista

lista.append("hola") #agrega un elemento al final de la lista

lista.insert(1, "insertar") #agrega un elemento en la posicion que se le pasa

lista.extend(["prueba", "25"]) #agrega varios elementos al final de la lista

lista.pop(0) #elimina el ultimo elemento de la lista

lista.remove("mundo") #elimina el elemento que se le pasa

# lista.sort() #ordena la lista pero si hay numeros y letras no se puede
# lista.sort(reverse=True) #ordena la lista en reversa

print(lista)