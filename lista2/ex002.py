"""Implemente e teste um programa que leia dois números inteiros e informe se o primeiro é múltiplo
do segundo. """

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

if(num1%num2 == 0):
    print("Eh multiplo!")
else:
    print("Nao eh multiplo.")