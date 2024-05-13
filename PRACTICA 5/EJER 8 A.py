def cantidad_de_div(num):
    suma=0
    for i in range(1,100):
        if num%i==0:
            suma=suma+1
    return suma


n=int(input("introduzca un numero: "))
print(cantidad_de_div(n))
