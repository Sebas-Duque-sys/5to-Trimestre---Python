class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_info(self):
        return f"Nombre: {self.nombre}. Edad: {self.edad}"

people = []

for i in range(2):
    print("Registro de personas.")
    nombre = str(input("Ingrese un nombre: ")) 
    while True:
        edad = int(input("Ingrese la edad: "))
        if edad > 0 and edad < 130:
            break
        else:
            print("Edad no valida.")
    p = Persona(nombre,edad)
    people.append(p)

print("\n--Lista de personas--")
for person in people:
    print(person.mostrar_info())