caracter=input("introduzca un caracter: ")
mensaje=input("introduzca una cadena/palabra: ")


resultado=""
for letra in mensaje:
    if letra in caracter:
        resultado=resultado+"*"
    else:
        resultado=resultado+letra

print(resultado)
