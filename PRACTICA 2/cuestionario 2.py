candidato = input("intrduzca su nombre: ")
resideEnBuenosAires= input("Reside en Buenos Aires?: ")
aniosDeExperiencia = int(input("Cuantos años de experiencia laboral tiene?: "))
palabraClave = input("Describase en una palabra")
puntajeAfinidad = float(input("Introduzca un muero en orden de merito"))
puntajeTotal = 0

if not resideEnBuenosAires:
    puntajeTotal+=1.6
    if aniosDeExperiencia > 10:
        puntajeTotal +=5.5
    else:
        puntajeTotal +=1.5
else:
    if palabraClave =="capo" or palabraClave=="leal":
        puntajeTotal +=2.1
    else:
        puntajeTotal +=0.5

puntajeTotal+=puntajeAfinidad

if puntajeTotal<2.5:
    print(candidato, "C")
else:
    print (candidato, "A")


