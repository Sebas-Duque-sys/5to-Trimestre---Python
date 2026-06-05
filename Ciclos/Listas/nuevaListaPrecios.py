#Lista        #0    #1    #2   #3
precios = [2000, 1500, 3000, 5000]
preciosConIva = []

for precio in precios:
    preciosConIva.append(precio*1.19)

print(f"Los precios con IVA son: {preciosConIva}")