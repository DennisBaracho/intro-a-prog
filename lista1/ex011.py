"""Implemente e teste um programa que leia um valor de despesa de restaurante, o valor da gorjeta (em porcentagem) e
o número de pessoas para dividir a conta, e imprima o valor que cada um deve pagar. Assuma que a conta será dividida
igualmente."""

despesa = float(input("Digite sua despesa no restaurante: "))
gorjeta = float(input("Digite a gorjeta: "))
nPessoas = int(input("Digite o numero de pessoas para dividir a conta: "))

contaIndividual = ((despesa*gorjeta)/100 + despesa)/nPessoas
print(f"\nCada pessoa pagará: {contaIndividual}")