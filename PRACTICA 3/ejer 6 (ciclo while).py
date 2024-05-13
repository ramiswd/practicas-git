n=int(input("Ingrese un número"))
i=1
cant_impares=0
suma=0
while(cant_impares<n):
    suma=suma+i #ACUMULADOR DE SUMAS
    print(i,suma)
    i=i+2 #GENERADOR DE IMPARES
    cant_impares=cant_impares+1 #CANTIDAD DE IMPARES


print("la suma final es:", suma)