"""Escreva um programa que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado."""
num = int(input(f"Digite o valor de numero 1: "))
numMaior = num
numMenor = num
contador = 1

while(contador != 50):
    contador += 1
    num = int(input(f"Digite o valor de numero {contador}: "))
    if(num < numMenor):
        numMenor = num
    elif(num > numMaior):
        numMaior = num

print(f"Maior numero: {numMaior}")
print(f"Menor numero: {numMenor}")