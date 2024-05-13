print("Este programa verifica si un anio es bisiesto")

anio = int(input("Ingrese un anio: "))

if(anio % 4 == 0):
    if(anio % 100 == 0 and anio % 400 != 0):
        print("el anio", anio, "es bisiesto")
    else:
        print("el anio", anio, "no Es bisiesto")
else:
       print("el anio", anio, "No es bisiesto")