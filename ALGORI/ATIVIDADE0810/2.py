print("Segunda Questão")

C= str(input("Código do trabalhador:"))
N= float(input("Horas trabalhadas: "))

if N <= 50:
    salario= N * 10
    print("Código do Trabalhador: %s, Horas trabalhadas: %s . Salário: R$ %s" %(C,N,salario))

else:
    excesso= (N-50)*20
    salario= (50*10) + excesso
    print("Horas trabalhadas: %s. Salário Total: R$ %s. Salário Excedente: R$ %s" %(N,salario,excesso))
