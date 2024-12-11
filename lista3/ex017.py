"""Escreva um algoritmo que lê um valor n inteiro e positivo, e calcula e escreve o valor de S para a
equação abaixo"""

n = int(input("Digite um valor inteiro e positivo: "))
fatorial = 1
contador = 0
s = 1

while n <= 0:
    n = int(input("Digite um valor inteiro e positivo: "))

while(contador != n):
    contador += 1
    fatorial *= contador
    s += 1/fatorial 

print(f"O valor de S é {s}")