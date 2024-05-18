def sinrep(lista):
    nuevalista=[]
    for i in range(len(lista)):
        if lista[i] not in nuevalista:
            nuevalista.append(lista[i])
    return nuevalista
            
lista=(1,2,3,4,4,4,4,7)

print(sinrep(lista))