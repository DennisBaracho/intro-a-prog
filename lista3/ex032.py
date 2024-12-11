"""Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles 
estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar 
quando for lido um número negativo ou maior que 100."""

num = 1
intervalo0a25 = 0
intervalo26a50 = 0
intervalo51a75 = 0
intervalo76a100 = 0

while num <= 100 and num >= 0:
    num = float(input("Digite um numero menor que 100 e positivo (maior que 100 ou negativo para encerrar leitura):"))
    if (num >= 0) and (num <= 25): 
        intervalo0a25 += 1
    elif (num >= 26) and (num <= 50):
        intervalo26a50 += 1
    elif (num >= 51) and (num <= 75):
        intervalo51a75 += 1
    elif (num >= 76) and (num <= 100):
        intervalo76a100 += 1

print(f"Total de numeros presentes no intervalo [0,25]: {intervalo0a25}\nTotal de numeros presentes no intervalo [26,50]: {intervalo26a50}\nTotal de numeros presentes no intervalo [51,75]: {intervalo51a75}\nTotal de numeros presentes no intervalo [76,100]: {intervalo76a100}.")