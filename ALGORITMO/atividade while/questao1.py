#Definindo váriaveis
nota=0
resposta= "sim"
volta= 0
soma=0

#Pedindo Nome do aluno
print("\n### Iniciando contagem! ###")
nome= input("Insira o nome do aluno: ")

#Dando inincio a contagem
while True:
    opcao= int(input("Deseja inserir uma nota? (sim-1 ou não-2)"))

    if opcao == 1:
        nota = float(input("Insira a nota: "))
        volta = volta + 1
        soma = soma + nota
    
    elif opcao == 2:
        break

    else:
        print("Opção inválida")

#Informando ao usuário o conteúdo
print("\n%s\nSoma das notas: %s\n" %(nome,soma))