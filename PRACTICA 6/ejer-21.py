s=[1,4.1,6.3,2,3.2,8]
x=3
def cantidad(lista,num):
    nueva=[]
    for elemento in lista:
        if num>elemento:
            nueva.append(0)
        else:
            nueva.append(elemento)
    return nueva


print(cantidad(s,x))