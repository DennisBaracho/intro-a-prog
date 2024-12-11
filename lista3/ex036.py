"""Escreva um algoritmo que leia 500 valores inteiros e positivos e: 
a. Encontre o maior valor;  
b. Encontre o menor valor;  
c. Calcule a média dos números lidos."""

contador = 0
media = 0
maiorNum = 0
menorNum = 0

while contador < 500:
    num = int(input("Digite um valor positivo e inteiro: "))
    if num < 0:
        while num < 0:
            num = int(input("Digite um numero inteiro e positivo: "))
    if contador == 0:
        maiorNum = num
        menorNum = num
    else:
        if num > maiorNum:
            maiorNum = num
        elif num < menorNum:
            menorNum = num
    media += num
    contador += 1

media /= 500

print(f"\nMaior valor lido: {maiorNum}\nMenor valor lido: {menorNum}\nMedia dos valores lidos: {media}")