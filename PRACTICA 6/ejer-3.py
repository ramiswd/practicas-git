def divisores(num):
    lista=[]
    for i in range (1,num+1):
        if num%i==0:
            lista=lista+[i]
    return lista

a=int(input("introduzca un num: "))

print(divisores(a))