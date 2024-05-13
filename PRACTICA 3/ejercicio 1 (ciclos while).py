print ("Vamos a realizar una division.")

a=int(input("elija un numero:"))
b=int(input("elija un numero:"))


while b==0:
    print ("b no puede ser cero.")

    b=int(input("elija un numero distinto de cero:"))

division=a/b
print(division)
