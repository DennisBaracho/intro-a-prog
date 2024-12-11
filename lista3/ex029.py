"""Escrever um algoritmo que leia um número não determinado de valores e calcule a média aritmética 
dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o 
percentual de valores negativos e positivos. Mostre os resultados."""

num = 1
positivos = 0
negativos = 0
media = 0

while(num != 0):
    num = float(input("Digite um numero: "))
    if num > 0:
        positivos += 1
        media += num
    elif num < 0:
        negativos += 1
        media += num
    else:
        print("Programa encerrado.")

total = positivos + negativos
media /= total

percentualN = (negativos*100)/total
percentualP = 100 - percentualN

print(f"Quantidade de numeros positivos lidos: {positivos}.\nQuantidade de numeros negativos lidos: {negativos}.\nMedia aritmetica: {media}.\nPercentual de numeros positivos: {percentualP}.\nPercentual de numeros negativos: {percentualN}.")