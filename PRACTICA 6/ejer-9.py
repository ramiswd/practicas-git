def maximo(lista):
    elMasGrande=lista[0]
    for elemento in lista:
        if elemento>elMasGrande:
            elMasGrande=elemento
    return elMasGrande

lista=[1,2,3,4,5,6,1000000,1100]

print(maximo(lista))