"""Modifique o programa anterior para imprimir a média aritmética com 3 casas decimais."""

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = int(input("Digite o terceiro numero inteiro: "))

media = (num1 + num2 + num3)/3

print(f"\nA media dos tres numeros eh: {round(media, 3)}")