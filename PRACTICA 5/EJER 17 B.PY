def aparece(caracter,cadena):
    if caracter in cadena:
        return True
    else:
        return False
    
letra=input("introduzca una letra: ")
palabra=input("introduzca una palabra: ")

print(aparece(letra,palabra))