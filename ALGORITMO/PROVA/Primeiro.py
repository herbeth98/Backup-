paes= float(input("Eae mano, quantos pães? "))

leite=float(input("Mano, quantos litros de leite? "))

dinheiro = float(input("Mano, você tem quantos reais? "))

valor_paes= (paes * 0.25)
valor_leite= (leite * 2.5)

soma= valor_leite + valor_paes
troco= (dinheiro - soma)

if troco < 0:
    print("Pães: R$ %s, Leite: R$ %s " + "Valor pago: R$ %s " + "Você está devendo: R$ %s"  %(valor_paes,valor_leite, soma, troco))

if (paes or leite or dinheiro) < 0:
    print("Valores inválidos!")

else:
    print("Pães: R$ %s, Leite: R$ %s ; Valor pago: R$ %s ; Seu troco é de: R$ %s"  %(valor_paes,valor_leite, soma, troco))

