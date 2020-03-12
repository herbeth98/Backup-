polu= float("Insira o nível de poluição: ")
if polu <0.25 and polu > 0.05:
    print("O nível está aceitável") 

elif polu > 0.3:
    print("As empresas do Grupo 1 devem suspender suas atividades!")
       
elif polu > 0.4:
    print("As empresas do Grupo 1 e do grupo 2 devem suspender suas atividades!")
            
else polu > 0.5:
    print("Todas as empresas devem suspender suas atividades!")

        