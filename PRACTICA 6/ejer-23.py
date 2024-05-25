def esta(caracter,listado):
    return caracter in listado

def cantApariciones(caracter,listado):
    cont=""
    for elem in listado:
        if caracter==elem:
            cont=cont+"*"
    return cont

def principal(cadena):
    caracteres=[]
    cantidades=[]
    for caracter in cadena:
        if not esta(caracter,caracteres):
            caracteres.append(caracter)
            cantidades.append(cantApariciones(caracter, cadena))
    for i in range (len(caracteres)):
        print(caracteres[i],":",cantidades[i])


principal("conocido")