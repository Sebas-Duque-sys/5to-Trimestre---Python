# productos = {
#     "Arroz: ":2500,
#     "Leche: ":1500,
#     "Pan: ":3000,
#     "Huevo: ":5000,
# }

# mayor = 0
# mayor_producto = ""
# for producto, precio in productos.items():
#     if precio > mayor:
#         mayor_producto = producto
#         mayor = precio

# print(f"Producto más costoso: {mayor_producto}{mayor}")

productos = {
    "Arroz: ":7500,
    "Leche: ":1500,
    "Pan: ":3000,
    "Huevo: ":5000,    
}

precios = list(productos.values())
mayor = precios[0]
mayor_producto = ""

for producto, precio in productos.items():
    if precio > mayor:
        mayor_producto = producto
        mayor = precio

print(f"Producto más costoso: {mayor_producto} - {mayor}")