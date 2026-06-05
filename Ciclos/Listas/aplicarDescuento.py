#Lista        #0    #1    #2   #3
productos = [2000, 1500, 3000, 5000]

for precio in productos:
    descuento = precio * 0.10
    nuevo_precio = precio-descuento
    print(f"Nuevo precio: {nuevo_precio}")
    
    