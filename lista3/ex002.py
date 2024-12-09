"""Elabore um programa que leia um número de entrada (n) que indicará a quantidade de números
a serem lidos. Em seguida, leia n números (conforme o valor informado anteriormente) e imprima
o triplo de cada um."""

n = int(input("Digite a quantidade de numeros a serem lidos: "))
contador = 0

while(contador < n): 
    num = int(input("Digite um numero: "))
    print(f"Triplo desse numero: {num*3}\n")
    contador += 1