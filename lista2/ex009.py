"""Implemente e teste um programa que leia 3 números inteiros e imprima uma das seguintes
mensagens: Todos os números são iguais;
Todos os números são diferentes;
Apenas dois números são iguais."""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if(num1 != num2) and (num1 != num3) and (num2 != num3):
    print("Todos os numeros sao diferentes.")
elif(num1 == num2) and (num2 == num3):
    print("Todos os numeros sao iguais")
else:
    print("Apenas dois numeros sao iguais.")