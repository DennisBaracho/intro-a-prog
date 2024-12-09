"""Escreva um programa que dado um número inteiro n calcule n! (fatorial) utilizando as estruturas
iterativas while, repeat-until e/ou for."""

num = int(input("Digite um numero para calcular o fatorial: "))
contador = 0
produto = 1

while(contador != num):
    contador += 1
    produto *= contador
    print(contador, end=" ")

print(f"Produto: {produto}")