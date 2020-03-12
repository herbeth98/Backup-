num1 = float(input("Ei mano, primeiro número:"))
num2 = float(input("Ei mano, segundo número:"))
num3 = float(input("Ei mano, terceiro número:"))
num4 = float(input("Ei mano, quarto número:"))

if num3 >= 1000:
    quad= (num3 * num3)
    print("%s²: %s" %(num3,quad))

else:
    quad1= num1*num1
    quad2= num2*num2
    quad3= num3*num3
    quad4= num4*num4
    print("%s²: %s" %(num1,quad1))
    print("%s²: %s" %(num1,quad2))
    print("%s²: %s" %(num1,quad3))
    print("%s²: %s" %(num1,quad4))