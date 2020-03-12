print("Primeira Questão:")

peso = float(input("Peso em KG: "))

if peso > 50:
    excesso = peso-50
    multa = excesso * 4
    print("O peso está acima do estabelecido, o peso excedente é de %s Kg e a multa é de R$ %s." %(excesso,multa))

else:
    excesso = 0
    multa = 0
    print("O peso está de acordo com o regulamento! Multa: %s. Excesso: %s" %(multa,excesso))
