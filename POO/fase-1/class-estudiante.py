#Una clase inicia con Mayuscula y no lleva parentesis
class Estudiante:
    #Esto se llama constructor, es lo que indica que se puede comenzar a llenar objetos con esta plantilla/clase
    def __init__(self,nombre,nota):
        #Aqui está haciendo que los valores ingresados se agreguen a las caracteristicas respectivas en la clase
        self.nombre = nombre
        self.nota = nota
    #Esto es un metodo, permite ejecutar la orden almacenada. El metodo solo utiliza los valores que se trasladaron a la clas
    def mostrar_info(self):
    #    return f"Nombre: {self.nombre} Nota: {self.nota}"
        if self.nota >= 3:
            estado = "Aprueba"
        else:
            estado = "Reprueba"
        return f"Nombre: {self.nombre} Nota: {self.nota} Estado: {estado}"

e1 = Estudiante("Juan",3.9)
print(e1.mostrar_info())