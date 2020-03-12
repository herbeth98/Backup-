resposta="sim"

pesoPeixe= 0

pesoTotal = 0

multa=0

excessoTotal= 0

quantidadePeixes= 0

while (resposta== "sim"):
    pesoPeixe= float(input("Informe o peso do peixe:"))
    if pesoPeixe > 50:
        excesso= pesoPeixe-50

        excessoTotal= excesso + excessoTotal
        
        multa= (excesso * 4 )+ multa

        pesoTotal= pesoPeixe + pesoTotal
        quantidadePeixes= quantidadePeixes + 1
        
        print("\nValor de sua multa atual: R$ %s \nExcesso de Peso total:%s Kg \nPeso Total da Pesca: %s Kg \nQuantidade de Peixes atual: %s" %(multa,excessoTotal,pesoTotal,quantidadePeixes))

    else:
        pesoTotal= pesoPeixe + pesoTotal
        quantidadePeixes= quantidadePeixes + 1

        print("\nVocê não foi multado por esse peixe! \nValor de sua multa atual: R$ %s \nExcesso de Peso total:%s Kg \nPeso Total da Pesca: %s Kg \nQuantidade de Peixes atual: %s" %(multa,excessoTotal,pesoTotal,quantidadePeixes))

    resposta= input("\nDeseja adicionar mais um peixe?(sim/não):")

print("Pesagem Finalizada!\nPeso total: %s Kg\nQuantidade de Peixes: %s\nValor total: R$%s"%(pesoTotal,quantidadePeixes,multa))

