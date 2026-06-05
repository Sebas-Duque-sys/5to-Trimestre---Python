productos = {
    "Arroz":2500,
    "Leche":1500,
    "Pan":3000,
    "Huevo":5000,    
}

for producto, precio in productos.items():
    if precio >= 3000:
        print(f"{producto} es caro. Su precio es de {precio} COP")