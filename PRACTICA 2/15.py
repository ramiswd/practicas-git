a=int(input("ingresar primer valor entero: "))
b=int(input("ingresar segundo valor entero: "))
c=int(input("ingresar tercer valor entero: "))


if a<b and a<c:
    menor=a
else:
    if b<a and b<c:
        menor=b
    else:
        menor=c

if a>b and a>c:
    mayor=a
else:
    if b>a and b>c:
        mayor=b
    else:
        mayor=c

if a>b and a<c or a<b and a>c:
    medio=a
else:
    if b>a and b<c or b<a and b>c:
        medio=b
    else:
        medio=c


a=menor
b=medio
c=mayor


print("de menor a mayor seria",a,b,c)