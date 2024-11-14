"""Implemente e teste um programa de caixa eletrônico que lê um valor e retorna o menor número de notas de R$50,
R$20 e R$10 que devem ser entregues ao correntista para somar aquele valor. Indique ainda o total entregue e o resto
que não poderá ser entregue (mesmo que seja 0). Exemplo de saída:"""

valor = float(input("Digite a quantia desejada: R$ "))
totalEntregue = 0

notas50 = (valor - totalEntregue)// 50
totalEntregue += 50*notas50

notas20 = (valor - totalEntregue)// 20
totalEntregue += 20*notas20

notas10 = (valor - totalEntregue)// 10
totalEntregue += 10*notas10

resto = valor - totalEntregue

print(f"Notas de 50 R$: {notas50}")
print(f"Notas de 20 R$: {notas20}")
print(f"Notas de 10 R$: {notas10}")
print(f"Total entregue: R$ {totalEntregue}")
print(f"Resto: R$ {resto}")