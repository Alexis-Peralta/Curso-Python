diccionario = {
    "nombre": "Alexis",
    "apellido": "Mandujano",
    "subs": 100000
}

# get es un metodo que nos permite obtener un valor de una clave
claves = diccionario.get("nombre")

# clear es un metodo que nos permite limpiar el diccionario
diccionario.clear()

#pop es un metodo que nos permite eliminar un elemento de un diccionario
diccionario.pop("subs")

diccionario_iterable = diccionario.items()

print(diccionario_iterable) # Alexis

