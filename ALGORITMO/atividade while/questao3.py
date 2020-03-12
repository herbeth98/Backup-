while True:
    opcao = input("Deseja informar um numero? sim/não ")
    if opcao == ("sim"):
        numero= int(input("\nInforme o número: "))

        if (numero%2) ==0:
            info="Par"
                    
        else:
            info="Ímpar"

    elif opcao == "não":
        break

    else:
        print("Opção inválida")
        

        
