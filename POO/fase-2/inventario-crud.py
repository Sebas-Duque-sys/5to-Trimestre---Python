class Productos:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
    def mostrar_info(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Categoria: {self.categoria}"
    
class SistemaInventario:
    def __init__(self):
        self.productos = []
    #1. Registrar producto
    def registrar_producto(self):
        codigo = str(input("Ingrese el código del producto: "))
        for prod in self.productos:
            if prod.codigo == codigo:
                print("El código ya existe. Intente con otro.")
                return
        nombre = str(input("Ingrese el nombre del producto: "))
        while True:
            precio = float(input("Ingrese el precio del producto: "))
            if precio >= 0:
                break
            else:
                print("Precio no válido. Intentelo nuevamente.")
        while True:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad >= 0:
                break
            else:
                print("Cantidad no válida. Intentelo nuevamente.")
        categoria = str(input("Ingrese la categoría del producto: "))
        nuevo_producto = Productos(codigo, nombre, precio, cantidad, categoria)
        self.productos.append(nuevo_producto)
        print("Producto registrado exitosamente.")
    #2. Mostrar productos
    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\nLista de productos:")
            for prod in self.productos:
                print(prod.mostrar_info())
    #3. Buscar producto
    def buscar_producto(self):
        codigo_buscar = str(input("Ingrese el código del producto a buscar: "))
        for prod in self.productos:
            if prod.codigo == codigo_buscar:
                print("Producto encontrado:")
                print(prod.mostrar_info())
                return
        print("Producto no encontrado.")
    #4. Actualizar producto
    def actualizar_producto(self):
        codigo_buscar = str(input("Ingrese el código del producto a actualizar: "))
        for prod in self.productos:
            if prod.codigo == codigo_buscar:
                print("Producto encontrado. Ingrese los nuevos datos:")
                while True:
                    prod.precio = float(input("Ingrese el nuevo precio del producto: "))
                    if prod.precio >= 0:
                        break
                    else:
                        print("Precio no válido. Intentelo nuevamente.")
                while True:
                    prod.cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    if prod.cantidad >= 0:
                        break
                    else:
                        print("Cantidad no válida. Intentelo nuevamente.")
                prod.categoria = str(input("Ingrese la nueva categoría del producto: "))
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")
    #5. Eliminar producto
    def eliminar_producto(self):
        codigo_buscar = str(input("Ingrese el código del producto a eliminar: "))
        for prod in self.productos:
            if prod.codigo == codigo_buscar:
                self.productos.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")
    #6. Calcular valor total del inventario
    def calcular_valor_inventario(self):
        if len(self.productos) == 0:
            print("No hay productos registrados para calcular el valor del inventario.")
        else:
            valor_total = 0
            for prod in self.productos:
                valor_total += prod.precio * prod.cantidad
            print(f"El valor total del inventario es: {valor_total:.2f}")
    #7. Mostrar productos agotados
    def mostrar_productos_agotados(self):
        agotados = []
        for prod in self.productos:
            if prod.cantidad == 0:
                agotados.append(prod)
        if len(agotados) == 0:
            print("No hay productos agotados.")
        else:
            print("\nProductos agotados:")
            for prod in agotados:
                print(prod.mostrar_info())
    #8. Guardar archivo
    #Investigar más acerca de está posibilidad
    def guardar_archivo(self):
        with open("productos.txt", "w") as archivo:
            for prod in self.productos:
                archivo.write(prod.mostrar_info() + "\n")
        print("Archivo guardado exitosamente.")
    #9. Menu para interactuar con el sistema
    def menu(self):
        while True:
            print("""
MENU
1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Calcular valor total del inventario
7. Mostrar productos agotados
8. Guardar archivo
9. Salir
            """)
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_producto()
            elif opcion == "5":
                self.eliminar_producto()
            elif opcion == "6":
                self.calcular_valor_inventario()
            elif opcion == "7":
                self.mostrar_productos_agotados()
            elif opcion == "8":
                self.guardar_archivo()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break

#Activador inicial
SistemaInventario().menu()