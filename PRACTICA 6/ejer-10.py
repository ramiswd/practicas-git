def MaximoIndice(lista):
    maxIndice=0
    maxElem=lista[0]

    for i in range (len(lista)):
        if lista[i]>maxElem:
            maxElem=lista[i]
            maxIndice=i
    return maxIndice

lista=[1,2,190,10,20,21]

print(MaximoIndice(lista))