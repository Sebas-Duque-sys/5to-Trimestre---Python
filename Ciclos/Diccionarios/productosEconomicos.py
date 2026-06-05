productos = {
    "Arroz: ":2500,
    "Leche: ":1500,
    "Pan: ":3000,
    "Huevo: ":5000,    
}

contador = 0
for precio in productos.values():
    if precio <= 2000:
        contador += 1

print(f"Productos baratos: {contador}")