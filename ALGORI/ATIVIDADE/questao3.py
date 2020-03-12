prod1= input("Nome do produto 1:")
preco1= float(input("Preço do produto %s: " %prod1))

prod2= input("Nome do produto 2:")
preco2= float(input("Preço do produto %s: " %prod2))

prod3= input("Nome do produto 3:")
preco3= float(input("Preço do produto %s: " %prod3))

#Se os preços forem iguais! 
if preco1 == preco2 and preco2 == preco3:
    print("Os valores dos produtos são iguais!")

elif preco1 == preco2 and preco2 < preco3:
    print("Escolha entre %s ou %s, pois são mais baratos!" %(prod1,prod2))

elif preco1 == preco3 < preco2:
    print("Escolha entre %s ou %s, pois são mais baratos!" %(prod1,prod3))

elif preco3 == preco2 < preco1:
    print("Escolha entre %s ou %s, pois são mais baratos!" %(prod2,prod3))

elif preco3 < preco2 and preco2 < preco1:
    print("Escolha %s, pois é mais barato!" %(prod3))

elif preco2 < preco3 and preco3 < preco1:
    print("Escolha %s, pois é mais barato!" %(prod2))

else:
    print("Escolha %s, pois é mais barato!" %(prod1))