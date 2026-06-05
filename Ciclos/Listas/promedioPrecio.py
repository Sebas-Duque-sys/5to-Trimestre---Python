#Lista        #0    #1    #2   #3
precios = [2000, 1500, 3000, 5000]

calculo = 0
for precio in precios:
    calculo += precio

calculo /= len(precios)

print(f"El promedio de precios es: {calculo}")