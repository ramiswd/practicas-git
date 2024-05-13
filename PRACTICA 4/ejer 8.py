nombre=input("introduzca su nombre: ")
apellido=input("introduzca su apellido: ")
dni=input("introduzca su DNI: ")

nueva=""

for letra in dni:
    if len(nueva)<3:
        nueva=nueva+letra

nueva=nueva+"_"
cont=0

for letra in apellido:
    if cont<3:
        nueva=nueva+letra.upper()
        cont=cont+1

cont=1
for letra in nombre:
    if cont==1 or cont==len(nombre):
        nueva=nueva+letra.upper()
    cont=cont+1

print(nombre,apellido,dni,"la contraseña nueva es:",nueva)