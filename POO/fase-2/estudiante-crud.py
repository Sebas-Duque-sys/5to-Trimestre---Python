class Estudiante:
    #Constructor para inicializar los atributos del estudiante
    def __init__(self,codigo,nombre,nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota
    #Método para actualizar la nota del estudiante
    def estado(self):
        if self.nota >= 3:
            return "Aprueba"
        else:
            return "Reprueba"
    #Método para mostrar la información del estudiante
    def mostrar_info(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Nota: {self.nota}, Estado: {self.estado()}"

class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = []
    #1. Registrar estudiante
    def registrar_estudiante(self):
        #Solicitar y validar el código del estudiante para evitar duplicados
        codigo = str(input("Ingrese el código del estudiante: "))
        for est in self.estudiantes:
            #Necesito Explicación de la siguiente linea---------------------------------
            if est.codigo == codigo:
                print("El código ya existe. Intente con otro.")
                return
        #Solicitar el nombre del estudiante
        nombre = str(input("Ingrese el nombre del estudiante: "))
        #Solicitar y validar la nota del estudiante
        while True:
            nota = float(input("Ingrese la nota del estudiante: "))
            if 0 <= nota <= 5:
                break
            else:
                print("Nota no válida. Intentelo nuevamente.")
        
        #Crear un nuevo estudiante y agregarlo a la lista de estudiantes
        #Crear una variable, llamar a clase Estudiante y asignar los valores que se acaban de solicitar
        nuevo_estudiante = Estudiante(codigo, nombre, nota)
        #Agregar la variable que contiene el objeto con el nuevo estudiante a la lista de estudiantes
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante registrado exitosamente.")
    #2. Mostrar estudiantes
    def mostrar_estudiantes(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for est in self.estudiantes:
                print(est.mostrar_info())
    #3. Buscar estudiante
    def buscar_estudiante(self):
        #Definir codigo a buscar
        codigo_buscar = str(input("Ingrese el código del estudiante a buscar: "))
        #Llamar a todos los estudiantes registrados
        for est in self.estudiantes:
            #Comparar el código de cada estudiante con el código a buscar
            if est.codigo == codigo_buscar:
                #Si se encuentra el estudiante, mostrar su información y salir del método
                print("Estudiante encontrado:")
                print(est.mostrar_info())
                return
        #Si no se encuentra el estudiante después de revisar toda la lista, mostrar mensaje de no encontrado
        print("Estudiante no encontrado.")
    #4. Eliminar estudiante
    def eliminar_estudiante(self):
        #Solicitar el código del estudiante a eliminar
        codigo_buscar = str(input("Ingrese el código del estudiante a eliminar: "))
        #Recorrer la lista de estudiantes
        for est in self.estudiantes:
            #Si el código del estudiante coincide con el código a eliminar, sigue.
            if est.codigo == codigo_buscar:
                #Llamar lista de estudiantes y eliminar el estudiante que se recorre actualmente
                self.estudiantes.remove(est)
                print("Estudiante eliminado exitosamente.")
                return
        print("Estudiante no encontrado.")
    #5. Actualizar nota estudiante
    def actualizar_nota(self):
        codigo_buscar = str(input("Ingrese el código del estudiante para actualizar la nota: "))
        for est in self.estudiantes:
            if est.codigo == codigo_buscar:
                #Solicitar y validar la nueva nota del estudiante
                while True:
                    nueva_nota = float(input("Ingrese la nueva nota del estudiante: "))
                    if 0 <= nueva_nota <= 5:
                        #Llamar la nota del estudiante que se esta recorriendo y actualizar con la nueva nota ingresada
                        est.nota = nueva_nota
                        print("Nota actualizada exitosamente.")
                        return
                    else:
                        print("Nota no válida. Intentelo nuevamente.")
        print("Estudiante no encontrado.")
    #6. Calcular promedio
    def calcular_promedio(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados para calcular el promedio.")
        else:
            #Comando final
            #total_notas = sum(est.nota for est in self.estudiantes)
            suma = 0
            for est in self.estudiantes:
                suma += est.nota
            promedio = suma/len(self.estudiantes)
            #Que es :.2f
            print(f"El promedio de las notas es: {promedio:.2f}")
    #7. Guardar archivo
    #######################INVESTIGAR COMO FUNCIONA ESTO#######################
    def guardar_archivo(self):
        with open("estudiantes.txt", "w") as archivo:
            for est in self.estudiantes:
                archivo.write(est.mostrar_info() + "\n")
        print("Archivo guardado exitosamente.")
    #8. Estadísticas
    def estadisticas(self):
        aprobados = 0
        reprobados = 0
        for est in self.estudiantes:
            if est.estado() == "Aprueba":
                aprobados += 1
            else:
                reprobados += 1
        print(f"\n-- ESTUDIANTES --")
        print(f"Aprobados: {aprobados}")
        print(f"Reprobados: {reprobados}")
    #9. Menu para interactuar con el sistema de estudiantes
    def menu(self):
        while True:
            print("""
            MENU
            1. Registrar estudiante
            2. Mostrar estudiantes
            3. Buscar estudiante
            4. Eliminar estudiante
            5. Actualizar nota
            6. Calcular promedio
            7. Guardar archivo
            8. Estadisticas
            9. Salir
            """)
            #Metodo con Match
            #opcion = int(input("Seleccione una opción: "))
            #match opcion:
            #    case 1:
            #        self.registrar_estudiante()
            #    case 2:
            #        self.mostrar_estudiantes()
            #    case 3:
            #        self.buscar_estudiante()
            #    case 9:
            #        print("Saliendo del sistema...")
            #        return
            #    case _:
            #        print("Opción no válida. Intente nuevamente.")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.registrar_estudiante()
            elif opcion == 2:
                self.mostrar_estudiantes()
            elif opcion == 3:
                self.buscar_estudiante()
            elif opcion == 4:
                self.eliminar_estudiante()
            elif opcion == 5:
                self.actualizar_nota()
            elif opcion == 6:
                self.calcular_promedio()
            elif opcion == 7:
                self.guardar_archivo()
            elif opcion == 8:
                self.estadisticas()
            elif opcion == 9:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

SistemaEstudiantes().menu()