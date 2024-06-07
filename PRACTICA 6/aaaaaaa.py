cantidad=int(input("introduzca un num: "))

numerador=1
denominador=3
serie=0

for termino in range(cantidad):
    x=termino+numerador
    fraccion=x/denominador**x
    if termino%2!=0:
        fraccion=fraccion*(-1)
    serie=serie+fraccion

print(serie)



        
        

        
