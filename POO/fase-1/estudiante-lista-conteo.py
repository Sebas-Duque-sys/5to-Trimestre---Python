class Estudiante:
    contadorAprobados = 0
    contadorReprobados = 0
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        if self.nota >= 3:
            Estudiante.contadorAprobados += 1
        else:
            Estudiante.contadorReprobados += 1
    def mostrar_info(self):
        if self.nota >= 3:
                estado = "Aprueba"
        else:
            estado = "Reprueba"
        return f"Nombre: {self.nombre} Nota: {self.nota} Estado: {estado}"

student = []

for i in range(3):
    print(f"\nRegistro del estudiante {i+1}")
    nombre = str(input("Nombre: "))
    while True:
        nota = float(input("Nota: "))
        if nota >= 0 and nota <= 5:
            break
        else:
            print("Nota no valida.")
    
    e = Estudiante(nombre,nota)
    student.append(e)

print("\nLista de estudiantes:")
for est in student:
    print(est.mostrar_info())

print("\n--- Resumen ---")
#Una clase tambien puede almacenar variables.
print("Aprobados: ", Estudiante.contadorAprobados)
print("Reprobados: ", Estudiante.contadorReprobados)