a=int(input("introduzca un numero: "))
b=int(input("introduzca un numero: "))
c=int(input("introduzca un numero: "))
print("usted ingreso:", a, b, c)

print(a, 22"es mayor que", b, a>b)
print(a, "es el mayor de todos", a>b and a>c)
print(b, "es el menor de todos",b<a and b<c )
print(a, "es mayor que alguno de los otros dos", a>b or a>c and a<b or a>c)
print(a, "es menor o igual que alguno de los otros dos" , a<=b or a<=c)
print("Los tres numeros son iguales", a==b==c)
print("Los tres numeros son distintos", a!=b!=c)
print(a, "es par", a%2==0 )
print("alguno es par",a%2==0 or b%2==0 or c%2==0)
print(ninguno es par, True)
print("todos son pares", a%2==0 and b%2==0 and c%2==0)
print(a,"es multiplo de 3", a%3==0)
print(a,"es multiplo de 3 y 5", a%3==0 and a%5==0)
print(a,"es multiplo de 3 y es par", a%3==0 and a%2==0)
print(a,"-",b,"da un numero positivo", a>b)
print(a,"-",b,"da un numero par positivo", a>b and a%2==0 or b%2==0)