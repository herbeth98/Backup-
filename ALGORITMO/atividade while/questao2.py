#Definindo váriaveis
nota=0
soma= nota
resposta= "sim"
volta= 0
media=0

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



#Condição de aprovação pela média
media= soma/volta
if media >= 7:
    aprov = "Aprovado"
elif media <7 and media >=4:
    aprov = "Recuperação"
else:
    aprov = "Reprovado"

#Informando ao usuário o conteúdo
print("\n \n%s\nSoma das notas: %s\nQuantidade de Notas: %s \nMédia das Notas: %s - %s" %(nome,soma,volta,media,aprov))