"""Desenvolva um programa que leia dois valores a e b (a <= b) e mostre os seguintes resultados:
a. Todos os números em [a,b].
b. Todos os números ímpares em [a,b].
c. Todos os números ímpares em [a,b] e múltiplos de 3."""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
contador = num1

while(num1 > num2):
    num1 = int(input("Digite o primeiro numero novamente, ele precisa ser menor ou igual ao segundo: "))

print("\na. Todos os numeros em [a,b]:", end=" ")
while(contador <= num2):
    print(contador, end=" ")
    contador += 1

contador = num1

print("\nb. Todos os numeros impares em [a,b]:", end=" ")
while(contador <= num2):
    if(contador % 2 == 0):
        print(contador, end=" ")
    contador += 1

contador = num1

print("\nc. Todos os numeros impares em [a,b] e multiplos de 3:", end=" ")
while(contador <= num2):
    if(contador % 2 == 0) and (contador % 3 == 0):
        print(contador, end=" ")
    contador += 1