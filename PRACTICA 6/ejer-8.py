def cant(lista):
    cont=0
    for num in lista:
        cont+=1
    return cont

def promedio (lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    return suma

lista=[1.12,9.50,10]

print(promedio(lista)/cant(lista))