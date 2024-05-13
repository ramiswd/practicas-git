def mayor(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    else:
        if num2>=num1 and num2>=num3:
            return num2
        else:
            return num3

a=int(input("introduzca un num: "))
b=int(input("introduzca un num: "))
c=int(input("introduzca un num: "))
print(mayor(a,b,c))