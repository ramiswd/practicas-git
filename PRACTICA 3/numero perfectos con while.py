print("este programa busca los numeros perfectos")
n=int(input("introduzca el nuemro para ver si es perfecto"))
i=1
suma=0
while i<n:
    if n%i==0:
        suma=suma+i
    i=i+1

if suma==n:
    print("es p")
else:
    print("no es p")