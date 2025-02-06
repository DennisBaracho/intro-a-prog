'''Escreva uma função chamado TROCA que receba 2 variáveis inteiras (X e Y) e troque o
conteúdo entre elas'''

def troca(a,b):
    return (b,a)

def main():
    x, y = (input("Digite as variaveis inteiras na mesma linha: ")).split()
    x = int(x)
    y = int(y)
    x, y = troca(x,y)
    print(f"A variavel x agora vale: {x}, a variavel y agora vale: {y}")

main()