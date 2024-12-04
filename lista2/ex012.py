"""A loja Pegue&Pague resolveu aumentar sua promoção de aniversário. As compras feitas com
pagamento em dinheiro terão um desconto adicional de 5%. Modifique o programa anterior para
que seja lido também o tipo de pagamento (1 - dinheiro, 2 - cartão e 3 - cheque). Se o pagamento
for em dinheiro deve ser aplicado o desconto adicional de 5%."""

valorTotal = float(input("Valor total da sua compra: "))
tipoPagamento = int(input("\nDigite o tipo de pagamento:\n1 - Dinheiro\n2 - Cartao\n3 - Cheque\n"))

if(valorTotal < 50):
    valorDescontado = valorTotal*95/100
elif(valorTotal >= 50 and valorTotal <= 100):
    valorDescontado = valorTotal*90/100
else:
    valorDescontado = valorTotal*85/100

if(tipoPagamento == 1):
    valorDescontado = valorDescontado*95/100

desconto = round(valorTotal - valorDescontado, 2)

print(f"Total de desconto: R${desconto} Valor a ser pago: R${round(valorDescontado,2)}")
