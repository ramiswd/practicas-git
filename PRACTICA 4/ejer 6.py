palabra=input("introducir palabra: ")
caracter=input("introduzca un caracter que queres que se censure: ")

suma=""
for letra in palabra:
    if letra==caracter:
        suma=suma+"*"
    else:
        suma=suma+letra

print(suma)