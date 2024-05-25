def frecuencia (lista,num):
    cont=0
    for elemento in lista:
        if elemento==num:
            cont+=1
    return cont

lista=[1,2,2,2,2,3,4,5,6]
a=2

print(frecuencia(lista,a))