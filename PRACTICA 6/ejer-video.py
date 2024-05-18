def divisoresPropios(num):
    divisores=[]
    for i in range (1,num):
        if num%i==0:
            divisores.append(i)
    return divisores

a=int(input("introduzca un num: "))

print(divisoresPropios(a))
