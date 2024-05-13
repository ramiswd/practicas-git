def tres_veces(cadena):
    for i in range(3):
        print(cadena)


import math
def raizcuadrada(num):
    print(math.sqrt(num))


def promedio2(num1,num2,):
    return (num1+num2)/2

def promedio3(num1,num2,num3):
    return (num1+num2+num3)/3


def potencia(num1,num2):
    return num1**num2


def mayor(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    else:
        if num2>=num1 and num2>=num3:
            return num2
        else:
            return num3
        


def cantidad_de_div(num):
    suma=0
    for i in range(1,100):
        if num%i==0:
            suma=suma+1
    return suma




def suma_div(num):
    suma=0
    for i in range(1,num+1):
        if num%i==0:
            suma=suma+i
    return suma

def numero_perfecto(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma=suma+i
    return suma 

def cartel(palabra):
   print((len(palabra)+4)*"*")
   print("*",palabra,"*")
   return((len(palabra)+4)*"*")

def repeticion_letra(palabra,caracter):
    suma=0
    for letra in palabra:
        if letra==caracter:
            suma=suma+1
    return suma

