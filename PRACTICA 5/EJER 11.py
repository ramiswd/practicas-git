def suma_div(num):
    suma=0
    for i in range(1,num+1):
        if num%i==0:
            suma=suma+i
    return suma

n=int(input("introduzca un numero: "))

print(suma_div(n))