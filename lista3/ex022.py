"""Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3
centímetros por ano. Construa um programa que calcule e imprima quantos anos serão necessários
para que Zé seja maior que Chico."""

alturaChico = 1.50
alturaZe = 1.10
anos = 0

while(alturaZe < alturaChico):
    alturaZe += 0.03
    alturaChico += 0.02
    anos += 1

print(f"Serao necessarios {anos} anos para Ze ser maior que Chico")