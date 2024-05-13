nombre=input("introduzca su nombre")

vocales="aeiou"
suma=""

for letra in nombre:
    if letra not in vocales:
        suma=suma+letra

cont=""
while cont<4:
    cont=cont+"*"

import random

w=random.randrange(1,10)

contraseña=suma+cont+str(w)

print(contraseña)