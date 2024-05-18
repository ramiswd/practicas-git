def lamascorta(lista1,lista2):
    if len(lista1)>len(lista2):
        return lista2
    else:
        return lista1
    
animales=["gato","perro","paloma"]

planetas=["jupirter","Saturno","Tierra","Marte"]

print(lamascorta(animales,planetas))