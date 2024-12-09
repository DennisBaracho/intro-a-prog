"""Faça um programa que leia o nome de um aluno, a quantidade de provas realizadas por ele e suas
respectivas notas. O algoritmo deve apresentar ao final o nome e a média das notas obtidas do
aluno.
Obs.: Utilize a função gets para fazer leitura de strings."""

nome = input(("Digite o nome do aluno: "))

qtdProvas = 0
soma = 0
contador = 0

while(qtdProvas <= 0):
    qtdProvas = int(input("Digite quantas provas o aluno realizou: "))

while(contador != qtdProvas):
    contador += 1
    nota = float(input(f"Digite sua nota na prova {contador}: "))
    soma += nota

media = soma/qtdProvas
print(f"A media das notas obtidas pelo aluno {nome} foi: {media}.")