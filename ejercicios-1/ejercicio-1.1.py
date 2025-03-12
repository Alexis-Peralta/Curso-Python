#promedio de duración de cursos
otros_curos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# duracion de crudos

crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duración

diferencia_con_min= 100 - dalto_curso / otros_curos_min * 100
diferencia_con_max= 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio= 100 - dalto_curso / otros_cursos_promedio * 100

# Tiempo removido de los cursos

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

# Mostrando las diferencias de duración

print("-----------------")
print("La diferencia de duración de los cursos es de: ", diferencia_con_min, "%")
print("La diferencia de duración de los cursos es de: ", diferencia_con_max, "%")
print("La diferencia de duración de los cursos es de: ", diferencia_con_promedio, "%")
print("-----------------")

#Mostrando el tiempo removido de los cursos

print("El tiempo removido de los cursos es de: ", tiempo_vacio_promedio, "%")
print (f"Este curso elimininó el {tiempo_vacio_dalto} % de los cursos")
print("-----------------")

#Mostrando diferencias si los cursos duraran 10 horas

print(f"Si los cursos duraran 10 horas, la diferencia de duración sería de: {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver:  {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")