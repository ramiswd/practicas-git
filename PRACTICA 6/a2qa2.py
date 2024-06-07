def SinVocales(cadena):
    vocales="aeiou"
    resultado=""
    for letra in cadena:
        if letra not in vocales:
            resultado+=letra
    return resultado
def esta(cadena):
    nueva=""
    for char in cadena:
        if char not in nueva:
            nueva+=char
    return nueva
        
def CodigoLetra(nombre):
    codigo= SinVocales(nombre)
    codigo=esta(codigo)
    return codigo.upper()

def AgregarCeros(numero):
    numero_str=str(numero)
    cerosnec=4-len(numero_str)
    if cerosnec>0:
        numero_str="0"*cerosnec+numero_str
    return numero_str

def AgregarNumero(numero):
    if numero>9999:
        return str(numero)[-4:]
    else:
        aux=AgregarCeros(numero)
        return aux

nombre=input("introduzca el nombre del libro")
paginas=int(input("introduzca las paginas que tiene el libro"))

CodigoFinal=(CodigoLetra(nombre)+AgregarNumero(paginas))
print(CodigoFinal)
