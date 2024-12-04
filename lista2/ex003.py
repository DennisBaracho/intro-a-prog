"""Implemente e teste um programa que leia o estoque mínimo de um produto e o estoque atual e
exiba a situação do produto: abaixo do estoque, no limite ou acima do estoque."""

estoqueMin = int(input("Digite o estoque minimo do produto: "))
estoqueAtual = int(input("Digite o estoque atual do produto: "))

if(estoqueAtual > estoqueMin):
    print("Acima do estoque.")
elif(estoqueAtual < estoqueMin):
    print("Abaixo do estoque.")
else:
    print("Estoque no limite!")
