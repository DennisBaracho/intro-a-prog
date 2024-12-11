"""Faça um programa que leia dois valores inteiros valor inteiro e , calcule e mostre:"""

x = int(input("Digite x: "))
n = int(input("Digite n: "))
i = 1 
soma = 0

while (i <= n):
    soma += x 
    i += 1
    
print(f"Resultado da letra a): {soma}\n")

x = int(input("Digite x: "))
y = int(input("Digite y: "))
n = int(input("Digite n: "))
i = 1 
soma = 0

while (i <= n):
    soma += x*y
    i += 1
    
print(f"Resultado da letra b): {soma}\n")

x = int(input("Digite x: "))
n = int(input("Digite n: "))
i = 1 
soma = 0

while (i <= n):
    soma += x**2
    i += 1
    
print(f"Resultado da letra c): {soma}")
