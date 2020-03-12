num1= int(input("Insira o 1º número: "))
num2= int(input("Insira o 2º número: "))

if num1 == num2:
    print("Os valores são iguais!")

elif num1 < num2:
    print("O número maior é: %s" %num2)

else:
    print("O número maior é: %s" %num1)