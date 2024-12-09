"""Faça um programa que imprima a média de n números (n é um valor lido do teclado) excluindo
o menor e o maior deles. Seu programa deve tratar casos em que n < 3 exibindo uma mensagem
de erro."""

n = int(input("Digite a quantidade de numeros que serao lidos para calcular a media: "))


while(n < 3):
    n = int(input("Erro! Digite um numero maior ou igual a 3: "))

num = int(input("Digite um numero: "))
soma = num
numMaior = num
numMenor = num
contador = 1

while(contador != n):
    contador += 1
    num = int(input("Digite um numero: "))
    if(num < numMenor):
        numMenor = num
    elif(num > numMaior):
        numMaior = num
    soma += num

soma -= numMenor
soma -= numMaior
n -= 2
media = soma/n
print(f"A media eh: {media}")