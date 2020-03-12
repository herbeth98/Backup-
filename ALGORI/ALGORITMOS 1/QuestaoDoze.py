#Escrever um algoritmo que lê o nº de matrícula de um vendedor de uma empresa,
#  seu salário fixo e o total de vendas do vendedor. O vendedor recebe um salário fixo,
#  mais uma comissão proporcional as vendas por ele efetuadas. 
# A comissão é de 3 % sobre o total de vendas até 1.000 e 5 % 
# sobre o que ultrapassa este valor. Escrever o nº do vendedor, o total de suas vendas,
#  seu salário fixo e seu salário total.

funcionario = int (input ('Informe sua ID como profissional (ID):   '))
totalVendas = int ( input ( 'Informe seu total em vendas no mês:   '))
salarioFixo = float ( input ('Informe o seu salario fixo: '))

if (totalVendas<900):
        comissao = (3/100) * totalVendas
else:
    comissao = (3/100) * totalVendas + (totalVendas - 1000) * 5/100


salario_total = salarioFixo + comissao

print('Vendedor:%s - Total de Vendas:%s - Salário Fixo:R$%s - Salário Final:R$%s'%(funcionario,totalVendas,salarioFixo,salario_total))