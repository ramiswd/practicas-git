def numeroPrimo(n):         
    cant=0
    for i in range(1,n+1):
        if n%i==0:
            cant=cant+1
    if cant==2:
        return True
    else:
        return False

def primerosFactoresPrimos(n):
    cantPrimos=1
    primos=[]
    i=2
    while cantPrimos<= n:
        if numeroPrimo(i):          
            primos.append(i)
            cantPrimos=cantPrimos+1
        i=i+1
    return primos

n=int(input("Ingrese un numero"))

print(n,"=",primerosFactoresPrimos(n))


