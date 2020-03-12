def menu():
    print("\n** Menu **\n")
    print("1 - Cadastrar produtos")
    print("2 - Apagar Produto")
    print("3 - Listar todos os produtos")
    print("4 - Pesquisar Produto")
    print("5 - Vender produtos")
    print("6 - Encerrar venda")
    print("7 - Exibir Estoque")
    print("8 - Sair")

#lista de produtos
produtos = [] 
# Função para cadastrar produtos
def cadastrar(produto,preco,qnt):
    produtos.append(produto)
    produtos.append(qnt)
    produtos.append(preco)
    print("\n### Cadastro realizado com sucesso! ###\n")


def apagar_produto(produto):
    if produto in produtos:
        #Pegando indice
        indice_produto_removido= produtos.index(produto)
        produtos.remove(produto) #Removendo produto
        produtos.pop(indice_produto_removido) #Removendo quantidade
        produtos.pop(indice_produto_removido) #Removendo preço
        print("\nProduto removido com sucesso! \n")

    else:
        print("\nProduto não encontrado ou nome Incorreto!\n")

def listar_produtos():
    tamanho_lista= len(produtos)
    contador = 0

    print ("\n***LISTA DE PRODUTOS***\n")

    for produto_est in produtos:
        contador = contador + 1

        if contador == 1:
            print("Produto: %s" %produto_est)

        elif contador == 3:
            contador = 0
            print("Valor: %s\n" %produto_est)



def pesquisar_produto(produto_pesquisar):
    if produto_pesquisar in produtos:
        indice_produto= (produtos.index(produto_pesquisar) + 1)
        indice2_produto= (produtos.index(produto_pesquisar) + 2)
        preco_produto = produtos[indice2_produto]
        quant_produto = produtos[indice_produto] 
        print("\n%s - Contém: %s unidades e custa: R$ %s/cada \n" %(produto_pesquisar,quant_produto,preco_produto))
    else:
        print("Produto não encontrado ou nome Incorreto!")


compra=[]


def vender_produto(cliente,produto_comprar):
    
    if produto_comprar in produtos:
      
        if cliente in compra:

            indice_cliente = compra.index(cliente)
            preco_compras= produtos[(produtos.index(produto_comprar)) + 2]
            carteira = compra[indice_cliente+1] - preco_compras
            indice_quantidade =  produtos.index(produto_comprar) + 1
            reduzindo_quantidade = produtos[indice_quantidade] - 1
            produtos.pop(indice_quantidade)
            produtos.insert(indice_quantidade,reduzindo_quantidade)

            compra.insert((indice_cliente+1),carteira)
            compra.insert((indice_cliente+2),produto_comprar)

            print("\nProduto adicionado ao carrinho do cliente!\n") 
            print("O produto %s custa: R$ %s\nSaldo do cliente após compra: R$ %s" %(produto_comprar,preco_compras,carteira))
            
        else:
            carteira = float(input("Informe o saldo do cliente: "))
            
            compra.append(cliente)#cadastrar o cliente
            indice_cliente = compra.index(cliente)
            preco_compras= produtos[(produtos.index(produto_comprar)) + 2]
            carteira = carteira - preco_compras
            indice_quantidade =  produtos.index(produto_comprar) + 1
            reduzindo_quantidade = produtos[indice_quantidade] - 1
            produtos.pop(indice_quantidade)
            produtos.insert(indice_quantidade,reduzindo_quantidade)

            compra.insert((indice_cliente+1),carteira)
            compra.insert((indice_cliente+2),produto_comprar)

            print("\nProduto adicionado ao carrinho do cliente!\n") 
            print("O produto %s custa: R$ %s\nSaldo do cliente após compra: R$ %s" %(produto_comprar,preco_compras,carteira))

    else:
        print("\nProduto não existente!\n")

def encerrar_venda():
    cliente_encerrar = input("Insira o cliente à fechar o carrinho: ")
    if cliente_encerrar in compra:
        indice_cliente_encerrar = compra.index(cliente_encerrar)
        carteira_cliente_encerrar = compra[indice_cliente_encerrar + 1]
        print("\nCliente: " +cliente_encerrar+"\nLista de Produtos: \n Troco: R$ %s" %carteira_cliente_encerrar)

        for produto_lista in compra:
            if produto_lista == cliente_encerrar or produto_lista == carteira_cliente_encerrar:
                produto_lista = "vazio"

            elif produto_lista in produtos or produto_lista == "vazio":
                print(produto_lista)

            else:
                break
        
    else:
        print("\nCliente não encontrado!\n")

        
def  exibir_estoque():
    contador = 0

    print ("\n***Estoque***\n")

    for produto_est in produtos:
        contador = contador + 1
        
        if contador == 1:
            print("Produto: %s" %produto_est)

        elif contador == 2:
            print("Quantidade: %s\n" %produto_est)

        else:
            contador = 0