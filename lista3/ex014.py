"""Elabore um programa que leia um número e imprima todos os números de 1 até o número lido, e também o seu produto.
Ex.:Número: 3 Saída: 1 2 3 Produto: 6"""

n = int(input("Digite quantos numeros serao contabilizados: "))
num = 0
contador = 0
produto = 1

while(contador != n):
    num += 1
    contador += 1
    produto *= num
    print(num, end=" ")

print(f"Produto: {produto}")