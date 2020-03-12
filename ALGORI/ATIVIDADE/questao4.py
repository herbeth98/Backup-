#4) Faça um algoritmo que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 > num3 and num3 > num2:
    print("%s > %s > %s " %(num1,num3,num2))

elif num1 > num2 and num2 > num3:
    print("%s > %s > %s " %(num1,num2,num3))

elif num2 > num1 and num1 > num3:
    print("%s > %s > %s " %(num2,num1,num3))

elif num2 > num3 and num3 > num1:
    print("%s > %s > %s " %(num2,num3,num1))
    
elif num3 > num1 and num1 > num2:
    print("%s > %s > %s " %(num3,num1,num2))

else:
    print("%s > %s > %s" %(num3,num2,num1))








