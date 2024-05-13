edad=int(input("introducir edad: "))
distancia=int(input("introducir distancia: "))

if edad>=18:
    if edad <=70:
        if distancia <=500:
            print("Puede votar.")
        else:
            print("safaste")
    else:
        print("safaste")
else:
    print("safaste")



