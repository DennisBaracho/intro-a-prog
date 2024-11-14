"""Implemente e teste um programa que leia um numero inteiro e imprima o seu antecessor e o seu sucessor, seguindo o formato descrito."""

num = int(input("\tEntre com um numero inteiro: "))

antecessor = num - 1
sucessor = num + 1

print(f"\t Seu antecessor eh: {antecessor}")

print(f"\t  Seu sucessor eh: {sucessor}")