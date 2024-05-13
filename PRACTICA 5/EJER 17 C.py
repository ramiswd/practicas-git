def canta(letra,cadena):
    cont=0
    for char in cadena:
        if char==letra:
            cont+=1
    return cont

a=input("introduzca una palabra: ")
b=input("introduzca un caracter")

print(canta(a,b))