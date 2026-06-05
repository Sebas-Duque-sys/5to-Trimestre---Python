#Lista        #0    #1    #2   #3
precios = [2000, 1500, 3000, 5000]

mayor = precios[0]
for p in precios:
    if mayor < p:  
        mayor = p

print(f"Precio más alto: {mayor}")