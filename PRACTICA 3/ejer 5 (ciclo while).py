n=int(input("Ingrese un número"))
i=1
suma=0
while(i<=n):
    suma=suma+i #ACUMULADOR DE SUMAS
    print(i,suma)
    i=i+2 #CONTADOR - VAR.DE CONTROL

print("la suma final es:", suma)
