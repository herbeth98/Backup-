from modulo_CredPay import *

while True:
    menu()
    opcao = int (input("\nInforme oque você quer fazer: "))

    if opcao == 1:
        nome_cliente = (input("Qual nome do cliente que vocẽ quer cadastrar? "))
        cpf_cliente = int (input("Informe o CPF do cliente: "))
        numero_cartao = int (input("Informe o numero do cartão do cliente: "))
        limite = int (input("Informe o limite do cartão: "))

        cadastrar_clientes(nome_cliente,cpf_cliente,numero_cartao,limite)

    elif opcao == 2:
        nome_cliente = input("Qual cliente você deseja apagar? ")

        deletar_cliente(nome_cliente)

    elif opcao == 3:
        listar_clientes(nome_cliente)
    
    elif opcao == 4:
        cliente_pesquisar = int (input("Qual o CPF do cliente que você quer pesquisar? "))

        pesquisar_cliente(cliente_pesquisar)

    elif opcao == 5:
        cliente_add_credito = input("Informe o nome do cliente que você quer adcionar créditos: ")
        valor_credito_add = float (input("Informe a quantidade de créditos que serão adcionados: "))

        adcionar_credito(cliente_add_credito,valor_credito_add)

    elif opcao == 6:
        num_cartao = int (input("Informe o numero do Cartão: "))
        valor_compra = float (input("Informe o valor da comprar: "))

        compra(num_cartao,valor_compra)
    
    elif opcao == 7:
        num_cartao = int (input("Informe o cartão do cliente: "))
        meses = int(input("Quantos meses já se passaram? "))
        
        render(num_cartao,meses)

    elif opcao == 8:
        cartao_cliente = int (input("Informe o numero do cartão do cliente: "))

        visualisar_limite(cartao_cliente)
        
    elif opcao == 9:
        break


        
