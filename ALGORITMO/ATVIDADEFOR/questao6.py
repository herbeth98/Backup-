print("###############\nCÁLCULO FATORIAL\n###############")
fatorial=1
num= int(input("Insira um número inteiro: "))

for voltas in range(num,0,-1):
    fatorial= fatorial * voltas
    
print("O número fatorial de %s é: %s" %(num,fatorial))