def esta(elem,lista):
    for valor in lista:
        if elem==valor:
            return True
    return False

def interseccion(lista1,lista2):
    nueva=[]

    for elem in lista1:
        if esta (elem,lista2):
            nueva.append(elem)
    return nueva

lista1=[1,2,3,4,5,6]
lista2=[2,4,6,7,8,]

print(interseccion(lista1,lista2))