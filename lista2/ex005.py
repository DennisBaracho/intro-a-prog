"""Implemente e teste um programa que leia 2 números inteiros e imprima o maior deles (se houver).
Suponha que os números são diferentes."""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if(num1 > num2):
    print(num1)
else:
    print(num2)