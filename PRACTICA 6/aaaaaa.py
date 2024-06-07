#creacion de la palabra
Salas= [ 1 , 2 , 3 , 4 , 5 , 6 ]
Peliculas = ["Xmen","Titanic","Saw","Rio","Taxi Driver","Avatar"] 
CapacidadDisponiblePorSala= [ 80 , 70 , 60 , 75 , 40 , 90 ]

def IndicePelis(persona,peliculas):
    for i in range(len(peliculas)):
        if persona==peliculas[i]:
            return i
    return "error"

persona=input("introduzca la pelicula que quiera ver: ")

if persona in Peliculas:
    entradas=int(input("Cuantas entradas quiere retirar?: "))
    indiceDeEntradas=IndicePelis(persona,Peliculas)
    if CapacidadDisponiblePorSala[indiceDeEntradas]>=entradas:
        print("La pelicula",persona,"En la Sala",Salas[indiceDeEntradas])
        CapacidadDisponiblePorSala[indiceDeEntradas]-=entradas
        print(CapacidadDisponiblePorSala)
    else:
        print("no tenemos suficientes entradas")
else:
    print("no tenemos esa pelicula en cartelera")






