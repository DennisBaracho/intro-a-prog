"""Escreva um programa que leia 5 pares de valores, o primeiro representando o número de um aluno, 
e o segundo representando a sua altura em centímetros. Seu programa deve encontrar o aluno 
mais alto e o mais baixo, mostrando o número do aluno mais alto e do mais baixo, juntamente com 
suas alturas."""

contador = 1
numMaisAlto = 0
numMaisBaixo = 0
altMaisAlto = 0
altMaisBaixo = 0
aluno1 = 0
aluno2 = 0
aluno3 = 0
aluno4 = 0
aluno5 = 0
numero = 0

while contador <= 5:
    numero, altura = input("Digite o numero e a altura do aluno em centimetros: ").split()
    numero = int(numero)
    altura = float(altura)   
    if contador == 1:
        aluno1 = numero
        numMaisAlto = numero
        altMaisAlto = altura
        numMaisBaixo = numero
        altMaisBaixo = altura
    elif contador == 2:
        aluno2 = numero
    elif contador == 3:
        aluno3 = numero
    elif contador == 4:
        aluno4 = numero
    elif contador == 5:
        aluno5 = numero
    if (numero == aluno1) and ((numero == aluno2) or (numero == aluno3) or (numero == aluno4) or (numero == aluno5)):
        while (numero == aluno2) or (numero == aluno3) or (numero == aluno4) or (numero == aluno5):
            numero = int(input("Digite um numero diferente dos anteriores: "))
    elif (numero == aluno2) and ((numero == aluno1) or (numero == aluno3) or (numero == aluno4) or (numero == aluno5)):
        while (numero == aluno1) or (numero == aluno3) or (numero == aluno4) or (numero == aluno5):
            numero = int(input("Digite um numero diferente dos anteriores: "))
    elif (numero == aluno3) and ((numero == aluno2) or (numero == aluno1) or (numero == aluno4) or (numero == aluno5)):
        while (numero == aluno2) or (numero == aluno1) or (numero == aluno4) or (numero == aluno5):
            numero = int(input("Digite um numero diferente dos anteriores: "))
    elif (numero == aluno4) and ((numero == aluno2) or (numero == aluno3) or (numero == aluno1) or (numero == aluno5)):
        while (numero == aluno2) or (numero == aluno3) or (numero == aluno1) or (numero == aluno5):
            numero = int(input("Digite um numero diferente dos anteriores: "))
    elif (numero == aluno5) and ((numero == aluno2) or (numero == aluno3) or (numero == aluno4) or (numero == aluno1)):
        while (numero == aluno2) or (numero == aluno3) or (numero == aluno4) or (numero == aluno1):
            numero = int(input("Digite um numero diferente dos anteriores: "))
   
    if altura > altMaisAlto:
        numMaisAlto = numero
        altMaisAlto = altura
    if altura < altMaisBaixo:
        numMaisBaixo = numero
        altMaisBaixo = altura
    contador += 1
print(f"\nNumero do aluno mais baixo: {numMaisBaixo}\nAltura do aluno mais baixo: {altMaisBaixo}\nNumero do aluno mais alto: {numMaisAlto}\nAltura do aluno mais alto: {altMaisAlto}")

