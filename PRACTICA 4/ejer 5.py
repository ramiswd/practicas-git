palabra=input("introduzca una palabra: ")
vocales="aeiou"
cont=0
haydiptongo=False

for letra in palabra:
    if letra in vocales:
        cont=cont+1
    else:
        cont=0

if cont==2:
    haydiptongo=True

if haydiptongo:
    print("la palabra",palabra,"tiene diptongo")
else:
    print("la palabra",palabra,"no tiene diptongo")