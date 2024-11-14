"""Implemente e teste um programa que leia duas notas de um aluno, calcule e imprima sua média, sabendo que a primeira
nota tem peso 3 e a segunda nota tem peso 7."""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = ((nota1*3) + (nota2*7))/10

print(f"A media das duas notas eh: {media}")