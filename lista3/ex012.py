"""Escreva um programa em que é declarada uma constante contendo o valor de pi (com 10 casas
decimais) e uma variável r, cujo valor deve ser fornecido pelo usuário. O programa calcula a área
do círculo e o mostra ao usuário. Isso é repetido varias vezes até que o usuário responda N (não)
para a pergunta: “Deseja calcular mais áreas? Sim (S) ou não (N)?”."""

import math
pi = float(round(math.pi, 10))

pergunta = 'S'
while(pergunta != 'N'):
    r = float(input("\nDigite o valor do raio: "))
    area = 2*pi*r
    print(f"A area do circulo de raio {r} eh: {area}")
    pergunta = input("Deseja calcular mais áreas? Sim (S) ou não (N)?")

print("Programa encerrado.")