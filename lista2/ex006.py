"""Implemente e teste um programa que leia 2 números inteiros e imprima o maior deles. Se eles
forem iguais, imprima uma mensagem adequada para o usuário"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if(num1 > num2):
    print(num1)
elif(num1 == num2):
    print("Numeros iguais")
else:
    print(num2)