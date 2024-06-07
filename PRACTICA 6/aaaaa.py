def mezclas(colores,costo):
    for i in range (len(colores)):
        for j in range (i+1,len(colores)):
            if colores[i]=="blanco" or colores[j]=="blanco":
                print("4 litros", colores[i]+"-"+colores[j]+" $"+str((((costo[i]+costo[j])/2)*4)+0.73))
            print("1 litro", colores[i]+"-"+colores[j]+" $"+str(((costo[i]+costo[j])/2)+0.62))


colores=["carmin","petroleo","gris","verde","blanco","azul"]
costo=[11,10,9,12,8,15]

mezclas(colores,costo)