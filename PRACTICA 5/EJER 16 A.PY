def repeticion_letra(palabra,caracter):
    suma=0
    for letra in palabra:
        if letra==caracter:
            suma=suma+1
    return suma

n=input("introduzca una palabra: ")
b=input("introduzca caracter: ")

print("la letra",b,"se repite",repeticion_letra(n,b),"veces")