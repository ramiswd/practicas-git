s=[1,2,3.20,6.99,7]
x=3.21
def cantidad(lista,num):
    nueva=[]
    for elemento in lista:
        if num>elemento:
            nueva.append(elemento)
    return len(nueva)


print(cantidad(s,x))