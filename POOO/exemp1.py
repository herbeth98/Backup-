valor_casa = float(input("Insira o valor da casa a comprar: R$ "))
salario = float(input("Insira o valor que você recebe(salário): R$ "))
anos = int(input("Insira a quantidade de anos na qual deseja pagar: "))

prestacao = valor_casa /(anos * 12)

if prestacao <= (salario * 0.3):
    print("Financiamento aprovado!")
else:
    print("Salário não aprovado: Salário abaixo dos 30% necessários")

print(f"Salário: R$ {salario}")
print(f"Prestação: R$ {salario}")
print(f"30% do Salário: {salario * 0.3 }")