

def menu():
    print ("      __MENU__      ")
    print ("1-Cadastrar Clientes")
    print ("2-Apagar cliente")
    print ("3-Listar todos os clientes")
    print ("4-Pesquisar cliente ")
    print ("5-Inserir crédito no cartão")
    print ("6-Realizar compra com o cartão")
    print ("7-Render dinheiro")
    print ("8-Visualizar limite do cartão")
    print ("9-Sair")

clientes = []
cartoes = []


def cadastrar_clientes(nome_cliente,cpf_cliente,num_cartao,limite_cartao):
    clientes.append(nome_cliente)
    clientes.append(cpf_cliente)

    cartoes.append(num_cartao)
    cartoes.append(limite_cartao)
    
    print("\n=-=-=-> Cliente Cadastrado Com Sucesso!!! <=-=-=- \n _____________________________________________________ \n ")


def deletar_cliente(nome_cliente):
        if nome_cliente in clientes:
                indice_cliente_removido = clientes.index(nome_cliente)
                clientes.remove(nome_cliente)
                clientes.pop(indice_cliente_removido)

                indice_limite_removido = (indice_cliente_removido+1)
                cartoes.pop(indice_limite_removido)
                cartoes.pop(indice_cliente_removido)
                
                print("\n=-=-=-=-=-=-= Cliente apagado com sucesso!!! =-=-=-=-=-=-=\n")
        else:
                print("\n=-=-=-=-=-=-= Cliente não encontrado=-=-=-=-=-=-= \n")
    

def listar_clientes(nome_cliente):
    print("\n ----Lista de clientes---- \n")
    if nome_cliente in clientes:
        print("-> %s " %clientes)

def pesquisar_cliente(cliente_pesquisar):
        if cliente_pesquisar in clientes:
                indice_cliente_pesquisado = clientes.index(cliente_pesquisar)
                nome_cliente_pesquisado = clientes[indice_cliente_pesquisado-1]

                num_cartao = cartoes[indice_cliente_pesquisado-1]
                indice_limite_cartao = cartoes.index(num_cartao)
                limite_cartao =cartoes[indice_limite_cartao+1]

                print("\n Dados do CFP: %s\n --> Nome do Pertencente: %s \n --> CPF: %s \n --> Numero do Cartão: %s\n --> Limite do Cartão: %s "%(cliente_pesquisar,nome_cliente_pesquisado,cliente_pesquisar,num_cartao,limite_cartao))
        else:
                print ("\n =-=-=-=> Cliente não encontrado!!! <=-=-=-= \n")

def adcionar_credito(cliente_add_credito,valor_creditos_add):
        if cliente_add_credito in clientes:
                indice_cliente = clientes.index(cliente_add_credito)
                limite_cartao = cartoes[indice_cliente+1]
                indice_limite_cartao = cartoes.index(limite_cartao)

                limite_cartao = limite_cartao + valor_creditos_add #Somando créditos
                cartoes[indice_limite_cartao] = limite_cartao #Guardando na lista o valor dos créditos adcionados       

                print("\n =-=-=> %s de Créditos Adcionados Ao Cartão Do Cliente %s!!! <=-=-= \n"%(valor_creditos_add,cliente_add_credito))
        else:
                print ("\n =-=-=-=> Cliente não encontrado!!! <=-=-=-= \n")

def compra(num_cartao,valor_compra):
        if num_cartao in cartoes:
                indice_cartao = cartoes.index(num_cartao)
                limite_cartao = cartoes[indice_cartao+1]
                indice_limite_cartao = cartoes.index(limite_cartao)

                if valor_compra > limite_cartao:
                        print("\n Saldo insuficiente!!! \n")

                elif valor_compra <= limite_cartao:
                        print("\n =-=-=-=-=> Saldo Sulficiente <=-=-=-=-= \n")
                        novo_limite_cartao = limite_cartao - valor_compra
                        cartoes[indice_limite_cartao] = novo_limite_cartao
                        print ("--> Saldo Restante: %s \n"%novo_limite_cartao)
        else:
             print("\n =-=-=-> Cartão não encontrado!!! <=-=-= \n")

def render(num_cartao,meses):
        if num_cartao in cartoes:
                indice_cartao = cartoes.index(num_cartao)
                saldo_cartao = cartoes[indice_cartao + 1]
                indice_saldo_cartao = cartoes.index(saldo_cartao)

                renda = (saldo_cartao / 30)
                renda_total = (renda * meses)

                novo_saldo = (saldo_cartao+renda_total)
                cartoes[indice_saldo_cartao] = novo_saldo
                print("\n =-=-=> Processo Completo <=-=-= \n")

        else :
                print("=-=-=-> Cartão não encontrado <-=-=-=")

def visualisar_limite(cartao_cliente):
        if cartao_cliente in cartoes:
                indice_cartao = cartoes.index(cartao_cliente)
                limite_cartao = cartoes[indice_cartao+1]

                nome_cliente = clientes[indice_cartao]
                cpf_cliente = clientes[indice_cartao+1]

                print("\n --> Nome do Cliente: %s CPF: %s\n --> Numero do Cartão: %s\n --> Limite de Créditos disponíveis: %s\n"%(nome_cliente,cpf_cliente,cartao_cliente,limite_cartao))
                

