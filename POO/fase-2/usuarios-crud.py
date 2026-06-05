class Usuario:
    def __init__(self, documento, nombre, correo, rol, estado):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.estado = estado

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []
    #1. Registrar usuario
    def registrar_usuario(self):
        documento = str(input("Ingrese el documento del usuario: "))
        for user in self.usuarios:
            if user.documento == documento:
                print("El documento ya existe. Intente con otro.")
                return
        nombre = str(input("Ingrese el nombre del usuario: "))
        correo = str(input("Ingrese el correo del usuario: "))
        while not correo or "@" not in correo:
            print("Correo no válido. Intente nuevamente.")
            correo = str(input("Ingrese el correo del usuario: "))
        rol = str(input("Ingrese el rol del usuario (admin/usuario): "))
        while rol not in ["admin", "usuario"]:
            print("Rol no válido. Intente nuevamente.")
            rol = str(input("Ingrese el rol del usuario (admin/usuario): "))
        estado = str(input("Ingrese el estado del usuario (activo/inactivo): "))
        while estado not in ["activo", "inactivo", "Activo", "Inactivo"]:
            print("Estado no válido. Intente nuevamente.")
            estado = str(input("Ingrese el estado del usuario (activo/inactivo): "))
        nuevo_usuario = Usuario(documento, nombre, correo, rol, estado)
        self.usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente.")
    #2. Mostrar usuarios
    def mostrar_usuarios(self):
        for user in self.usuarios:
            print(f"Documento: {user.documento}, Nombre: {user.nombre}, Correo: {user.correo}, Rol: {user.rol}, Estado: {user.estado}")
    #3. Buscar usuario
    def buscar_usuario(self):
        documento = str(input("Ingrese el documento del usuario a buscar: "))
        for user in self.usuarios:
            if user.documento == documento:
                print(f"Documento: {user.documento}, Nombre: {user.nombre}, Correo: {user.correo}, Rol: {user.rol}, Estado: {user.estado}")
                return
        print("Usuario no encontrado.")
    #4. Actualizar usuario
    def actualizar_usuario(self):
        documento = str(input("Ingrese el documento del usuario a actualizar: "))
        for user in self.usuarios:
            if user.documento == documento:
                print(f"Usuario encontrado. Documento: {user.documento}, Nombre: {user.nombre}, Correo: {user.correo}, Rol: {user.rol}, Estado: {user.estado}")
                nombre = str(input("Ingrese el nuevo nombre del usuario (deje en blanco para no cambiar): "))
                correo = str(input("Ingrese el nuevo correo del usuario (deje en blanco para no cambiar): "))
                rol = str(input("Ingrese el nuevo rol del usuario (deje en blanco para no cambiar): "))
                estado = str(input("Ingrese el nuevo estado del usuario (deje en blanco para no cambiar): "))
                if nombre != "":
                    user.nombre = nombre
                if correo != "":
                    while not user.correo or "@" not in user.correo:
                        print("Correo no válido. Intente nuevamente.")
                        user.correo = str(input("Ingrese el nuevo correo del usuario: "))
                    user.correo = correo
                if rol != "":
                    user.rol = rol
                if estado != "":
                    user.estado = estado
                print("Usuario actualizado exitosamente.")
                return
        print("Usuario no encontrado.")
    #5. Eliminar usuario
    def eliminar_usuario(self):
        documento = str(input("Ingrese el documento del usuario a eliminar: "))
        for user in self.usuarios:
            if user.documento == documento:
                self.usuarios.remove(user)
                print("Usuario eliminado exitosamente.")
                return
        print("Usuario no encontrado.")
    #6. Mostrar usuarios activos
    def mostrar_activos(self):
        activos = []
        for user in self.usuarios:
            if user.estado == "activo":
                activos.append(user)
        for user in activos:
            print(f"Documento: {user.documento}, Nombre: {user.nombre}, Correo: {user.correo}, Rol: {user.rol}")
    #7. Contar usuarios por rol
    def contar_usuarios_por_rol(self):
        roles = []
        for user in self.usuarios:
            if user.rol not in roles:
                roles.append(user.rol)
        for rol in roles:
            #Contar usuarios por rol utilizando comprensión de listas
            cantidad = len([user for user in self.usuarios if user.rol == rol])
            print(f"Rol '{rol}': {cantidad} usuarios")
    #8. Exportar usuarios a archivo .txt
    def guardar_archivo(self):
        with open("usuarios.txt", "w") as f:
            for user in self.usuarios:
                f.write(f"{user.documento},{user.nombre},{user.correo},{user.rol},{user.estado}\n")
    def menu(self):
        while True:
            print("""
MENU
1. Registrar usuario
2. Mostrar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Mostrar usuarios activos
7. Contar roles
8. Guardar archivo
9. Salir
            """)
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.registrar_usuario()
            elif opcion == 2:
                self.mostrar_usuarios()
            elif opcion == 3:
                self.buscar_usuario()
            elif opcion == 4:
                self.actualizar_usuario()
            elif opcion == 5:
                self.eliminar_usuario()
            elif opcion == 6:
                self.mostrar_activos()
            elif opcion == 7:
                self.contar_usuarios_por_rol()
            elif opcion == 8:
                self.guardar_archivo()
            elif opcion == 9:
                print("Saliendo del sistema...")
                break