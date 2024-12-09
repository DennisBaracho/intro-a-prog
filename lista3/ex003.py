"""Faça um programa que leia um valor n indicando a quantidade de valores a ler em seguida. Um
número deve ser lido por vez e seu programa deve classificá-lo como positivo ou negativo."""

n = int(input("Digite a quantidade de numeros a serem lidos: "))
contador = 0

while(contador < n): 
    num = int(input("Digite um numero: "))
    if(num > 0):
        print("O numero eh positivo!\n")
    elif(num < 0):
        print("O numero eh negativo!\n")
    else:
        print("O numero nao eh nem positivo nem negativo.\n")
    contador += 1