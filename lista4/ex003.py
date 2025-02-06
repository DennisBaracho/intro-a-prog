'''3. Escreva uma função chamado SINAL que receba como parâmetro um valor N inteiro e
escreva a palavra POSITIVO se N for um número maior que zero, NEGATIVO se N for menor
que zero, ou ZERO se N for igual a zero. Escreva um algoritmo que leia um número inteiro e, usando a função SINAL, mostre se ele é
maior, menor ou igual a zero.'''

def sinal(n):
    if n > 0:
        print("POSITIVO")
    elif n < 0:
        print("NEGATIVO")
    else: 
        print("ZERO")

def main():
    valor = int(input("Digite um inteiro: "))
    sinal(valor)
main()