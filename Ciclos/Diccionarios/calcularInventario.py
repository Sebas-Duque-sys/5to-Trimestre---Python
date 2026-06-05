productos = {
    "Arroz: ":2500,
    "Leche: ":1500,
    "Pan: ":3000,
    "Huevo: ":5000,    
}

total = 0
for precio in productos.values():
    total += precio
    
print(f"Total inventario: {total}")