num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

operacao = int(input("Informe a operação desejada: \n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\nOpção Desejada: "))

if operacao == 1:
    print(f"O resultado é igual a: {num1 + num2}")

elif operacao == 2:
    print(f"O resultado é igual a: {num1 - num2}")

elif operacao == 3:
    print("O resultado é igual a: %.1f" %(num1 / num2))

elif operacao == 4:
    print(f"O resultado é igual a: {num1 * num2}")

else:
    print("Opção inválida!")
    



