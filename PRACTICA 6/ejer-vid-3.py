def maximo(lista):
    max=lista[0]
    for elemento in lista:
        if elemento>max:
            max=elemento
    return max

lista=[2,3,3,6,8,9,230]

print(maximo(lista))