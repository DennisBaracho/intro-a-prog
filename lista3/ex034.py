"""Escreva um algoritmo que leia um número não determinado de valores (m), todos inteiros e 
positivos, um de cada vez. Se m for par, verificar quantos divisores possui e escrever esta 
informação. Se m for ímpar e menor do que 10, calcular e escrever o m!. Se m for ímpar e 
maior ou igual a 10 calcular e escrever a soma dos inteiros de 1 até m."""

m = 0
divisores = 0
fatorial = 1
soma = 0
contador = 0 
contadorD = 1
contadorF = 1
contadorS = 0

while m == m:
    m = int(input("Digite um numero inteiro e positivo: "))
    if m < 0:
        while m < 0:
            m = int(input("Digite um numero inteiro e positivo: "))

    if (m % 2 == 0):
        while contadorD <= m:
            if (m % contadorD == 0):
                divisores += 1
            contadorD += 1
        print(f"Numero de divisores de m: {divisores}")

    elif (m % 2 != 0) and (m < 10):
        while contadorF <= m:
            fatorial *= contadorF
            contadorF += 1
        print(f"O fatorial de m (m!) eh: {fatorial}")
    
    elif (m % 2 != 0) and (m >= 10):
        while contadorS <= m:
            soma += contadorS
            contadorS += 1
        print(f"A soma dos inteiros de 1 ate f eh: {soma}")