nota=int(input("Ingresar nota: "))
nota2=int(input("Ingresar nota: "))
nota3=int(input("Ingresar nota: "))

promedio= (nota+nota2+nota3)/3
if promedio <=6:
    if promedio >3:
        print ("debe rendir final")
    else:
        print ("chau")
else:
     print("aprobo")

