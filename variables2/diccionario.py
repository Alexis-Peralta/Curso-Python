#creando diccionario con dict()

diccionario = dict(nombre="Sergio", apellido="Perez")

#las listas son pueden ser claves

diccionario ={frozenset(["Alexis", "Mandujano"]): "Estudiante"}

#creando diccionario con fromkeys()

diccionario = dict.fromkeys(["nombre", "apellido"])
 
 #creando diccionario con fromkeys() y un valor por defecto "no se"
 
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario["nombre"])
