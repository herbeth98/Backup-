from moduloproduto import *

for volta in range(0,3):

    nome_produto = str(input("Insira o nome do produto: "))
    preco_produto = float(input("Insira o preço do produto: "))

    preco_barato =  menor_preco (preco_produto)

print("O produto mais barato é: R$ %s" %(nome_mais_barato,preco_barato))
