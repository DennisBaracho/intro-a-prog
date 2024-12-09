"""Faça um programa que calcule a média aritmética de vários valores inteiros positivos, inseridos
pelo usuário. O final da leitura acontecerá quando for lido um valor negativo."""

num = int(input("Digite um numero inteiro positivo, o calculo da media aritmetica sera encerrado ao receber um negativo:"))
qtdNumeros = 0
soma = num

while(num >= 0): 
    num = int(input("Digite um numero inteiro positivo (negativo para encerrar): "))
    qtdNumeros += 1
    if(num >= 0):
        soma += num

media = soma/qtdNumeros
print(f"A media aritmetica foi: {media}")