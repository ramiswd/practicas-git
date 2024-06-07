def MaximoIndice(lista,blanco):
    
    for i in range (len(lista)):
        if i==blanco:
            return i
    return -1
    
lista=[1,2,3,190,10,20,21]
blanco=3

print(MaximoIndice(lista,blanco))