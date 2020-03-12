#Definindo váriaveis
maior_altura = 0
altura2 = 0
nome_alta= ""
nome_2alta= ""

while True:
    nome = input("Informe o nome da candidata: ('FIM' para finalizar)")
   
#condição de resposta
    if nome == "FIM" or nome == "fim" or nome == "Fim":
        break

    else:
        altura = float(input("Informe a Altura de %s: " %nome))
        if altura > maior_altura:
            nome_2alta= nome
            nome_alta = nome
            altura2= maior_altura
            maior_altura= altura

        elif altura > altura2:
            altura2 = altura
#Dando as informações ao usuário
print("\nA maior altura é de %s com %s.\nA segunda maior altura é de %s com %s."%(nome_alta,maior_altura,nome_2alta,altura2))