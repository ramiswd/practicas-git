def esta (num,lista):
    encontre=False
    for elemento in lista:
        if elemento==num:
            encontre=True
    return encontre

lista=[1,2,3,4,5]

a=2

print(esta(a,lista))
