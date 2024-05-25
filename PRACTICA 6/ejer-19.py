def listafactores(n):
    factores=[]
    i=2
    while n >=i:
        if n%i==0:
            n=n/i
            factores.append(i)
        else:
            i=i+1
    return factores

a=20
print(listafactores(a))

