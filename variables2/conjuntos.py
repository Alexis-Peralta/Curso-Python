#creando un conjunto con set
#Los datos set no se pueden modificar o mutar

conjunto = set(["dato1"])

conjunto1 = frozenset(["dato1", "dato2"]) # congelar el conjunto
conjunto2 = {conjunto1, "dato3"}

print("-------------------------------------------------")
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {4, 6, 8}

#Verificando si un subconjunto

# resultado = conjunto2.issubset(conjunto1)
# resultado = conjunto2 <= conjunto1
print("-------------------------------------------------")

#Verificar si un conjunto es un superconjunto

resultado = conjunto2.issuperset(conjunto1)
# resultado = conjunto1 > conjunto2

#Verificar si existe un resultado en comun

resultado = conjunto2.isdisjoint(conjunto1) #sera true si no hay elementos en comun

print(resultado)