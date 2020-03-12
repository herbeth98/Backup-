email = str(input("Insira seu email: "))
indice = email.index("@")
provedor = email[indice+1:]

ponto = provedor.index(".")

provedor_final= provedor[:ponto]



print("Provedor é: %s" %provedor_final)