def tieneRepetidas(palabra,caracter):
    suma=0
    for letra in palabra:
        if letra==caracter:
            suma=suma+1
        if suma>=2:
            return True
        else:
            return False
        
a=input("ingrese una palabra: ")
b=input("introduzca una letra: ")

print(tieneRepetidas(a,b))