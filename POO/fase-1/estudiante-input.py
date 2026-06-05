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

nombre = str(input("Ingrese el nombre. "))
nota = float(input("Ingrese la nota. "))

e1 = Estudiante(nombre,nota)
print(e1.mostrar_info())