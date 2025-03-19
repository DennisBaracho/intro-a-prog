'''12. Faça um algoritmo que leia um lista G[13] que é o gabarito de um teste da loteria esportiva, contendo os valores 1 quando for coluna 1, 0 quando for coluna do meio e 2 quando for coluna 2. Ler a seguir, para 10 apostadores, o número do cartão de cada apostador e um lista R[13] que seriam as respostas dos apostadores. Para cada apostador, mostre o número de acertos.

13. Com relação ao exercício anterior, calcule e mostre o percentual dos apostadores que fizeram de 10 a 13 pontos e o percentual dos apostadores que fizeram menos do que 10 pontos.'''

def main():
    g = []
    acertos = 0
    maisDe10 = 0
    resultado = ""
    for _ in range(13):
        novoG = int(input())
        g.append(novoG)

    for _ in range(10):
        r = []
        nCartao = int(input())
        for _ in range(13):
            novoR = int(input())
            r.append(novoR)

        for i in range(len(r)):
            if r[i] == g[i]:
                acertos += 1

        if acertos >= 10 and acertos <= 13:
            maisDe10 += 1
    
        resultado += (f"Cartao {nCartao}: {acertos} acertos.\n")
        acertos = 0

    percentualMaisDe10 = round((maisDe10*100/13),2)
    resultado += (f"Um total de {percentualMaisDe10}% fez de 10 a 13 pontos, {(100-percentualMaisDe10)}% fizeram menos de 10 pontos.")
    print(resultado)
main()