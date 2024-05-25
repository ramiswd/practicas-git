def intercambiar (s,a,b):
    aux=s[a]
    s[a]=s[b]
    s[b]=aux


lista=[1,2,3,4,5]

intercambiar(lista,3,4)
print(lista)