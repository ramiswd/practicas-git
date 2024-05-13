def cartel(palabra):
   print((len(palabra)+4)*"*")
   print("*",palabra,"*")
   return((len(palabra)+4)*"*")

   

a=input("introduzca una palabra: ")

print(cartel(a))