"""Construa um programa (com estrutura de repetição) que leia dois números (BASE e EXPOENTE)
e retorne como resultado a POTENCIA do cálculo da BASE elevado ao EXPOENTE.
Ex: para a BASE = 2 e EXPOENTE = 4, POTENCIA = 24 = 16."""

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = 1
contador = 0

while(contador < expoente):
    contador += 1
    potencia *= base

print(f"BASE = {base} e EXPOENTE = {expoente}, POTENCIA = 2^{expoente} = {potencia} ")