numero= int(input("Insira um número:"))

if numero == 0:
    print("O numero é NEUTRO")

elif numero > 0:
    dif= "Positivo"

else:
    dif= "Negativo"
    
if numero%2 == 0:
    print("O número %s é PAR e %s" %(numero,dif))
else:
    print("O número %s é IMPAR e %s" %(numero,dif))
