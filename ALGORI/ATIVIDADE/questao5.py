nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))

media = (nota1 + nota2)/2

if media > 10:
    print("Média inválida!")

elif media <= 10 and media >= 9:
    print("Aluno aprovado! Nota 1: %s, nota 2: %s, Média: %s, CONCEITO A" %(nota1,nota2,media))

elif media >= 7.5:
    print("Aluno aprovado! Nota 1: %s, nota 2: %s, Média: %s, CONCEITO B" %(nota1,nota2,media))

elif media >= 6:
    print("Aluno aprovado! Nota 1: %s, nota 2: %s, Média: %s, CONCEITO C" %(nota1,nota2,media))

elif media >= 4:
    print("Aluno repovado! Nota 1: %s, nota 2: %s, Média: %s, CONCEITO D" %(nota1,nota2,media))
    
else:
    print("Aluno aprovado! Nota 1: %s, nota 2: %s, Média: %s, CONCEITO E" %(nota1,nota2,media))