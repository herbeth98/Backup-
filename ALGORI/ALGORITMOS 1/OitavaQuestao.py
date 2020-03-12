codigo1 = str(input('Código da Peça:  '))

peca1 = str(input('Nome da Peça:  '))

qntMinima= int(input('Quantidade Mínima: '))

qntMaxima= int(input('Quantidade Máxima: '))

valorpeca = int(input("Valor da Peça:"))

media= (qntMaxima + qntMinima)/2

Total = media * valorpeca

print('Produto: %s; Custo médio do Estoque: %s ; Média do Estoque: %s '%(peca1,Total,media))
