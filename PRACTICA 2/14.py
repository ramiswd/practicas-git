valor1=int(input("ingresar valor uno: "))
valor2=int(input("ingresar valor dos: "))


aux=valor1
valor1=valor2
valor2=aux

if valor1<valor2:
    print(valor2,"y", valor1)
else:
    print(valor1,"y",aux)