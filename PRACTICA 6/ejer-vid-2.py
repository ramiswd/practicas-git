def contador(lista,n):
    cont=0
    for elemento in lista:
        if elemento==n:
            cont+=1
    return cont

lista=[1,2,3,3,3,3,5,5,5,5,5,5,5,7]
a=int(input("introduzca un numero:"))

print(contador(lista,a))