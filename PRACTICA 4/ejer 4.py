palabra=input("introducir una palabra")
caracter=input("introducir un caracter")
suma=0

for letra in palabra:
    if letra==caracter:
        suma=suma+1

print(suma)