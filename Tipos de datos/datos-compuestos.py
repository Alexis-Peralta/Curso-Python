lista = ["Alexis", "Mandujano", True, 5.5]
tuple = ("Alexis", "Mandujano", True, 5.5)

# print (lista[0])

#esto es valido
lista [0] = "Alex"
print (lista)

#esto no es valido

# tuple[0] = "Alex" # No se puede modificar un dato de una tupla
print (tuple)

# creando un conjunto (set)

conjunto = {"Alexis", "Mandujano", True, 5.5} # tampoco se puede modificar y no se puede acceder a un elemento en especifico

#creando un diccionario

diccionario = {
#   key    : value
#   clave  : valor
    "nombre": "Alexis",
    "apellido": "Mandujano",
    "estudiante": True,
    "promedio": 5.5
}

print (diccionario["nombre"]) # se accede a un elemento en especifico