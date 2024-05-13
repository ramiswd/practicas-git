n=int(input("ingrese un numero: "))
m=int(input("ingrese un numero: "))

while n<m:
    print("n no puede ser menor que m")
    n=int(input("ingrese un nuevo valor para n: "))

while m<n-1:
    m=m+1
    print(m)