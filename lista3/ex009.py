"""Elabore um algoritmo que leia um valor x e logo após um número n que indicará a quantidade
de números a serem lidos após a leitura de n. Em seguida, leia n números (conforme o valor
informado anteriormente) e, ao final imprima se o elemento x aparece e sua posição, caso positivo."""

x = int(input("Digite o valor de x: "))
n = int(input("Digite quantos numeros devem ser lidos: "))
contador = 0
aparece = 0

while(contador != n):
    num = int(input("Digite um numero: "))
    contador += 1
    if num == x:
        aparece = 1

if aparece == 1:    
    print("O elemento x aparece entre os numeros lidos!")
else:
    print("O elemento x nao aparece entre os numeros lidos!")