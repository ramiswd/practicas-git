def cant (lista,elemento):
    cont=0
    for i in lista:
        if i==elemento:
            cont+=1
    return cont

def repetido(lista):
    for elemento in lista:
        if cant (lista, elemento)>=2:
            return True
    return False

lista=[1,2,3,4,5,5,5]

print(repetido(lista))
