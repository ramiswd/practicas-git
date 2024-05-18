def MaximoIndice(lista,blanco):
    encontre=0
    for i in range (len(lista)):
        if lista[i]==blanco:
            encontre=i
    return encontre
    
lista=[1,2,3,190,10,20,21]
blanco=3

print(MaximoIndice(lista,blanco))