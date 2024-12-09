"""Escreva um programa que leia n valores, um de cada vez, e conte quantos destes valores são
negativos, escrevendo esta informação na tela."""

n = int(input("Digite a quantidade de numeros a serem lidos: "))
contador = 0
negativos = 0

while(contador < n): 
    num = int(input("Digite um numero: "))
    if(num < 0):
        negativos += 1
    contador += 1
print(f"Contei {negativos} numeros negativos!")