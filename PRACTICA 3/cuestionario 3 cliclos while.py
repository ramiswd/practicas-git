n=int(input("ingrese el valor de los entrevistados: "))

i=1
suma=0

while i<=n:
    nombre=input("introduzca su nombre: ")
    edad=int(input("introduzca la edad: "))
    suma=suma+edad
    profesion=input("ingrese la profesion: ")
    ingresos_mesuales=int(input("ingresos mensuales: "))
    ingresos_finales=ingresos_mesuales*40/100
    print (nombre)
    print(edad)
    print(profesion)
    print("ingreso de cuota",ingresos_finales)
    i=i+1
prom=print("promedio de edad de los entrevistados",suma/n)