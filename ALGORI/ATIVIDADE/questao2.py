#2) Faça um algoritmo que seja capaz de identificar se uma letra é vogal ou consoante.

letra= str(input("Insira a letra: "))

if letra == 'a' or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra é uma vogal!")

else: 
    print("A letra é uma consoante!")