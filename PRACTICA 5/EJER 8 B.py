def sumadiv(num):
    suma=0
    for i in range(1,num+1):
        if num%i==0:
            suma=suma+1
    return suma

def esprimo(num):
    return sumadiv(num)==2


n=int(input("introduzca un num: "))

print(esprimo(n))