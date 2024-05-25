def cant(lista):
    cont=0
    for num in lista:
        cont+=1
    return cont

def suma (lista):
    total=0
    for elemento in lista:
        total=total+elemento
    return total

lista=[1.12,9.50,10]

promedio=suma(lista)/cant(lista)

print(promedio)