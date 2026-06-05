class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar_info(self):
        if self.nota >= 3:
                estado = "Aprueba"
        else:
            estado = "Reprueba"
        return f"Nombre: {self.nombre} Nota: {self.nota} Estado: {estado}"

#Lista para almacenar estudiantes
student = []

#Ciclo para almacenar multiples estudiantes
for i in range(3):
    print(f"\nRegistro del estudiante {i+1}")
    #Solicita datos
    nombre = str(input("Nombre: "))
    nota = float(input("Nota: "))
    
    #Llama a la clase y agrega los datos ingresados
    e = Estudiante(nombre,nota)
    #Guarda los datos en la lista creada anteriormente
    #Cada dato almacenado en la lista queda como "objeto", por lo que se requiere realizar los metodos de la clase para usarlos.
    student.append(e)

print("\nLista de estudiantes:")
#Recorre la lista de estudiantes y pasa cada valor por el metodo "mostrar_info()". La impresión la crea la orden del metodo.
for est in student:
    print(est.mostrar_info())
    
print(student)