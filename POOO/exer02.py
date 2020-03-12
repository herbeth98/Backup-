email = str(input("Insira seu email: "))

indice = email.index("@")

nomeusuario = email[:indice]

print("Usuário é: %s" %nomeusuario)