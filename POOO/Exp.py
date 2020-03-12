salario = float(input("Insira seu salário: R$ "))
idade = int(input("Insira sua Idade: "))

if salario >= 2000 and idade >= 18:
    condicao = "Empréstimo poderá ser APROVADO"

else:
    if salario < 2000 and idade < 18:
        condicao = "Empréstimo não aprovado! Causa: Salário e idade abaixo do necessário!"

    elif salario < 2000:
        condicao = "Empréstimo não aprovado! Causa: Salário abaixo do necessário!"

    else:
        condicao = "Empréstimo não aprovado! Causa: Idade abaixo do necessário!"

print (condicao)