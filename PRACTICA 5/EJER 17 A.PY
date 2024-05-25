def sumadeletras(palabra,caracter):
    suma=0
    for letra in palabra:
        if letra==caracter:
            suma=suma+1
    return suma
            
a=input("ingrese una palabra: ")
b=input("introduzca una letra: ")

if 2==sumadeletras(a,b):
    print("True")
else:
    print("False")

