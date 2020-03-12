
ano_nasc= int(input("Ei mano, que ano você nasceu?"))
ano_atual=int(input("Em que ano estamos?"))

idade= (ano_atual - ano_nasc)

if idade <= 0:
    print("Valores inválidos") 

else:
    print("Você tem %s anos" %idade)