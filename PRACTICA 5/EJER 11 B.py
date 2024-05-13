def numero_perfecto(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma=suma+i
    return suma   

n=int(input("introduzca un num: "))
if numero_perfecto(n)==n:
    print(n,"es Perfecto")
else:
    print(n,"No es perfecto")
