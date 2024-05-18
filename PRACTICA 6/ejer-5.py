def divisible(n,num):
    return n%num==0

def factores(n,lista):
    for elementos in lista:
        if not divisible(n,elementos):
            return False
    return True

lista=[1,2,5,10]

b=10

print(factores(b,lista))