# Precio original y precio con descuento
precio_original = 120  # Precio original del producto
precio_descuento = 12  # Precio con descuento aplicado

# Cálculo del porcentaje de descuento
descuento = 100 - (precio_descuento / precio_original * 100)

# Ahorro en dinero
ahorro = precio_original - precio_descuento

# Mostrar resultados
print("-----------------")
print(f"Precio original: ${precio_original}")
print(f"Precio con descuento: ${precio_descuento}")
print(f"Descuento aplicado: {descuento:.2f}%")  # Redondeamos a 2 decimales
print(f"Ahorro: ${ahorro}")
print("-----------------")

# Comparación de precios
if precio_descuento < precio_original:
    print("¡El descuento es válido! Ahorraste dinero.")
else:
    print("No hay descuento aplicado o el precio aumentó.")