caracter=input("introduzca un caracter: ")
cadena=input("introduzca una cadena/palabra: ")

suma=0

for letra in cadena:
    if letra==caracter:
        suma=suma+1

print(suma)
