class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

e1 = Estudiante("juan",4.2)
print("Nombre: ",e1.nombre)

e2 = Estudiante("Ana",3.8)
print("Nombre: ",e2.nombre)