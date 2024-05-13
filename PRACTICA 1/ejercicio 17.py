dinero=float(input("Dinero que quiera retirar $"))

print("usted va a retirar:","$",dinero)

mil=dinero//1000
dinero=dinero%1000

quinientos=dinero//500
dinero=dinero%500

doscientos=dinero//200
dinero=dinero%200

cien=dinero//100
dinero=dinero%100

cincuenta=dinero//50
dinero=dinero%50
print(mil,"de 1000")
print(quinientos,"de 500")
print(doscientos,"de 200")
print(cien,"de 100")
print(cincuenta,"de 50")
print("$",dinero,"Queda en la cuenta")