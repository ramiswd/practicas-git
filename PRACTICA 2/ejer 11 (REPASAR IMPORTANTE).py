primero=int(input("Ingrese primer numero: "))
segundo=int(input("Ingrese segundo numero: "))
tercero=int(input("Ingrese tercer numero: "))

if (primero>=segundo):
    if (primero>=tercero):
        print("el mas grande es: ",primero)
    else:
        print("el mas grande es: ",tercero)
else:
    if (segundo>=tercero):
        print("el mas grande es: ",segundo)
    else:
        print("el mas grande es: ", tercero)