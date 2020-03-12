from modulo_ZeMercados import *

while True:
    menu()
    op = input("\nEi man, informe opção: ")

    if op=="1":
        produto = input("\nInforme o nome do produto: ")
        preco = float(input("Informe o preço de %s: "%produto))
        qnt = int(input("Informe a quantidade de %s: " %produto))
        cadastrar(produto,preco,qnt)

    elif op=="2":
        produto_remover = input ("\nInforme o Produto que deseja remover: ")
        apagar_produto(produto_remover)

    elif op=="3":
        listar_produtos()

    elif op=="4":
        produto_pesquisar = input ("\nInforme o Produto que deseja pesquisar: ")
        pesquisar_produto(produto_pesquisar)

    elif op=="5":
        cliente= input("Informe o nome do cliente: ")
        produto_comprar = input("Informe o produto que deseja comprar: ")
        vender_produto(cliente,produto_comprar)

    elif op=="6":
        encerrar_venda()

    elif op=="7":
        exibir_estoque()

    elif op=="8":
        print("\nSistema desligado!\n")
        break
    
    else:
        print("Opção inválida")