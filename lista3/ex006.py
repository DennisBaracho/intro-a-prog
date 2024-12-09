"""Escreva um programa que calcule a média dos números digitados pelo usuário se eles forem pares.
Termine a leitura se o usuário digitar 0."""

num = float(input("Digite um numero, o calculo da media aritmetica sera encerrado ao receber 0:"))
qtdNumeros = 0
soma = 0

while(num != 0): 
    if(num % 2 == 0):
        soma += num
        qtdNumeros += 1
    num = float(input("Digite um numero (encerre digitando 0): "))
    
media = soma/qtdNumeros
print(f"A media aritmetica foi: {media}")