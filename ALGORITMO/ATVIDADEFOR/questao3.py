num = int ( input ("Informe um número inteiro: "))
proximo_num = num + 1
soma_t = 0
for volta in range (20):
    if proximo_num % 2 == 0:
        soma_t = proximo_num + soma_t
    proximo_num = proximo_num + 1
    
print ("A soma total dos 10 números par encontrados é: %s" %soma_t)