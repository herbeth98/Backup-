

def cifra(palavra):

    alfabeto = ['a','e','i','o','u','f']
    nova_palavra = ""

    for letra in palavra:
        novo_indice = (alfabeto.index + 3)

        nova_palavra = nova_palavra + novo_indice[novo_indice]
       
       
        if novo_indice > len(alfabeto):
            novo_indice = novo_indice - len(alfabeto)

    


    return nova_palavra
