"""Escreva um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir. 
Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor."""

n = 0
while n <= 0:
    print("Digite um numero diferente e maior que 0")
    n = int(input("Digite quantos valores deverao ser lidos: "))

contador = 0
fatorial = 1
contadorF = 1

while contador != n:
    contador += 1
    num = int(input(f"\nValor {contador}: "))
    if num <= 0:  
        print("Digite um numero diferente e maior que zero.")
        contador -= 1
    else:
        while contadorF <= num:
            fatorial *= contadorF
            contadorF += 1
        print(f"Numero\tFatorial\n{num}\t{fatorial}")