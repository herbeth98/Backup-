#Informe os dados da 1ª Candidata
nome1= input("Qual o nome da 1ª candidata? ")
idade1= int(input("Qual é a idade de %s? " %nome1))
altura1= float(input("Qual é a altura de %s? " %nome1))
peso1= float(input("Insira o peso de %s: " %nome1))

#Informe os dados da 2ª Candidata
nome2= input("Qual o nome da 2ª candidata? ")
idade2= int(input("Qual é a idade de %s? " %nome2))
altura2= float(input("Qual é a altura de %s? " %nome2))
peso2= float(input("Insira o peso de %s: " %nome2))

#Informe os dados da 3ª Candidata
nome3= input("Qual o nome da 3ª candidata? ")
idade3= int(input("Qual é a idade de %s?" %nome3))
altura3= float(input("Qual é a altura de %s? " %nome3))
peso3= float(input("Insira o peso de %s: " %nome3))

nota11=float(input("Jurado A insira a nota de %s: " %(nome1)))
nota12=float(input("Jurado B insira a nota de %s: " %(nome1)))
nota13=float(input("Jurado C insira a nota de %s: " %(nome1)))
media1= (nota11 + nota12 + nota13)/3

nota21=float(input("Jurado A insira a nota de %s: " %(nome2)))
nota22=float(input("Jurado B insira a nota de %s: " %(nome2)))
nota23=float(input("Jurado C insira a nota de %s: " %(nome2)))
media2= (nota21 + nota22 + nota23)/3

nota31=float(input("Jurado A insira a nota de %s: " %(nome3)))
nota32=float(input("Jurado B insira a nota de %s: " %(nome3)))
nota33=float(input("Jurado C insira a nota de %s: " %(nome3)))
media3= (nota31 + nota32 + nota33)/3

if (media1 or media2 or media3) >= 5 and (media1 or media2 or media3) <= 10:
    if media1 > media2 and media2 > media3:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome1,nome2,nome3))

    elif media1 > media3 and media3 > media2:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome1,nome3,nome2))

    elif media2 > media1 and media1 > media3:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome2,nome1,nome3))

    elif media2 > media3 and media3 > media1:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome2,nome3,nome1))

    elif media3 > media1 and media1 > media2:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome3,nome1,nome2))

    elif media1 == media2 and media2 == media3:
        print("Todas as notas são iguais")

    else:
        print("1º Lugar: %s; 2º Lugar: %s; 3º Lugar: %s" %(nome3,nome2,nome1))

else:
    print("Notas inválidas!")