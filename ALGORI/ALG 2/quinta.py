#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km, mostre uma msg dizendo que ele foi multado. 
# A multa vai custar 7,00R$ por cada km acima do limite.

velocidade= float(input("Insira sua velocidade em KM/H: "))

if velocidade >= 140:
    multa= (velocidade - 80) * 10
    print("Você foi multado por estar conduzindo acima do limite, Sua multa é de: R$ %s" %multa)

elif velocidade > 80 and velocidade < 140:
    multa= (velocidade - 80) * 7
    print("Você foi multado por estar conduzindo acima do limite, Sua multa é de: R$ %s" %multa)
    
else:
    print ("Você está nos limites da pista. Parabéns! ")
    