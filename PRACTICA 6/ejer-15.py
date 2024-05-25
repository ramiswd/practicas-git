listaa=[1,2,3,4,5]
lista=[1,2,3,4,5,6]



def sacarrep(lista1,lista2):
    suma=lista1+lista2
    nueva=[]
    for i in range(len(suma)):
        if suma[i] not in nueva:
            nueva.append(suma[i])
    return nueva

print(sacarrep(listaa,lista))
        



