"""Faça um algoritmo que leia vários números inteiros e positivos e calcule o produto dos números 
pares. O fim da leitura será indicado pelo número 0."""

num = 1
produto = 1

while num != 0:
    num = int(input("Digite um numero inteiro e positivo (0 para encerrar): "))
    if(num < 0):
        print("Apenas numeros positivos e inteiros.")
    elif(num == 0):
        print("Programa encerrado.")
    elif(num % 2 == 0):
        produto *= num

print(f"O produto dos numeros pares eh {produto}.")
