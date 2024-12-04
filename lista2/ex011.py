"""A loja de eletrodomésticos Pegue&Pague está com uma grande promoção de aniversário. De
acordo com o valor das compras dos clientes será dado um desconto progressivo. As faixas de
desconto são as seguintes:
. Compras até R$50,00 - desconto de 5%
. Compras de R$50,00 a R$100,00 - desconto de 10%
. Compras acima de R$100,00 - desconto de 15%
Implemente e teste um programa que leia o valor total da compra do cliente e imprima o valor de
desconto e o total a ser pago, de acordo com as faixas de desconto acima."""

valorTotal = float(input("Valor total da sua compra: "))

if(valorTotal < 50):
    valorDescontado = valorTotal*95/100
elif(valorTotal >= 50 and valorTotal <= 100):
    valorDescontado = valorTotal*90/100
else:
    valorDescontado = valorTotal*85/100

desconto = round(valorTotal - valorDescontado, 2)

print(f"Total de desconto: R${desconto} Valor a ser pago: R${round(valorDescontado,2)}")