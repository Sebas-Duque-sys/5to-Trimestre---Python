from src.estadistica import calcular_promedio
from src.estadistica import promedio_diccionario
from src.estadistica import contar_aprobado
from src.estadistica import clasificar_notas

datos = [10,15,20,25,30]

promedio_datos = calcular_promedio(datos)

print(f"El promedio de la lista es de: {promedio_datos}")

notas = {
    "Juan":3.3,
    "Ana":4.2,
    "Pedro":4.6,
    "Laura":3.9
}

promedio_notas = promedio_diccionario(notas)
print(f"El promedio de las notas es: {promedio_notas}")

aprobados = contar_aprobado(notas, 3.5)
print(f"El número de estudiantes aprobados es: {aprobados}")

clasificación_notas = clasificar_notas(notas)
print("Clasificación de notas:", clasificación_notas)