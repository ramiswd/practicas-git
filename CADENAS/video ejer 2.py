cadena=(input("introduzca una palabra"))
suma=0

for letra in cadena:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        suma=suma+1

print(suma)
