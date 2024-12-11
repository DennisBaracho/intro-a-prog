"""Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a 
quantidade de números pares e ímpares, a média de valores pares e a média geral dos números 
lidos. O número que encerrará a leitura será número 0."""

num = 1
pares = 0 
impares = 0
mediaPares = 0
mediaGeral = 0

while num != 0:
    num = int(input("Digite um numero inteiro e positivo (0 para encerrar): "))
    if(num == 0):
        print("Programa encerrado.")
    elif(num > 0):
        if(num % 2 == 0):
            pares +=1 
            mediaPares += num
        else:
            impares +=1 
        mediaGeral += num 
    else:
        print("Apenas numeros positivos.")

total = pares + impares

mediaPares /= pares
mediaGeral /= total

print(f"Contei {pares} numeros pares e {impares} numeros impares. A media dos numeros pares foi {mediaPares}, a media geral foi {mediaGeral}.")