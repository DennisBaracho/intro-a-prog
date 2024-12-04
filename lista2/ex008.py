"""Implemente e teste um programa que leia 2 números inteiros e os imprima em ordem decrescente"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if(num1 > num2):
    print(num2, num1)
elif(num1 < num2):
    print(num1, num2)
else:
    print(num1, num2)