"""Escreva um algoritmo que gera e escreva os números ímpares entre 100 e 200."""

num = 100

while num < 200:
    if num % 2 != 0:
        print(num)
    num += 1