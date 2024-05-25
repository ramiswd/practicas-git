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

def divisoresPropios(num):
    divisores=[]
    for i in range (1,num):
        if num%i==0:
            divisores.append(i)
    return divisores

def mostrarEnUnaLinea(lista):
   for elemento in lista:
      print(elemento,end=" ")


def divisores(num):
    lista=[]
    for i in range (1,num+1):
        if num%i==0:
            lista=lista+[i]
    return lista

def lamascorta(lista1,lista2):
    if len(lista1)>len(lista2):
        return lista2
    else:
        return lista1
    
def divisible(n,num):
    return n%num==0

def factores(n,lista):
    for elementos in lista:
        if not divisible(n,elementos):
            return False
    return True

def cant (lista,elemento):
    cont=0
    for i in lista:
        if i==elemento:
            cont+=1
    return cont

def repetido(lista):
    for elemento in lista:
        if cant (lista, elemento)>=2:
            return True
    return False

def MaximoIndice(lista,blanco):
    encontre=0
    for i in range (len(lista)):
        if lista[i]==blanco:
            encontre=i
    return encontre

def cant(lista):
    cont=0
    for num in lista:
        cont+=1
    return cont

def suma (lista):
    total=0
    for elemento in lista:
        total=total+elemento
    return total

promedio=suma(list)/cant(list)

def maximo(lista):
    elMasGrande=lista[0]
    for elemento in lista:
        if elemento>elMasGrande:
            elMasGrande=elemento
    return elMasGrande

def MaximoIndice(lista):
    maxIndice=0
    maxElem=lista[0]

    for i in range (len(lista)):
        if lista[i]>maxElem:
            maxElem=lista[i]
            maxIndice=i
    return maxIndice

def intercambiar (s,a,b):
    aux=s[a]
    s[a]=s[b]
    s[b]=aux

def esta(lista,elem):
    for valor in lista:
        if elem==valor:
            return True
    return False

def interseccion(lista1,lista2):
    nueva=[]

    for elem in lista1:
        if esta (elem,lista2):
            nueva.append(elem)
    return nueva

def numeroPrimo(n):         
    cant=0
    for i in range(1,n+1):
        if n%i==0:
            cant=cant+1
    if cant==2:
        return True
    else:
        return False