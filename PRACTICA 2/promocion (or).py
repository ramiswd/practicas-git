nota1=int(input("Ingresar nota: "))
nota2=int(input("Ingresar nota: "))
nota3=int(input("Ingresar nota: "))

promedio=(nota1+nota2+nota3)/3

if (promedio<4 or nota1<4 or nota2<4 or nota3<4):
    print("Recurso")
else:
    if (promedio<7):
        print("Rinde final")
    else:
        print("Promociona")