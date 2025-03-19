'''14. Faça um algoritmo que leia um conjunto de 30 valores. Para cada valor lido, coloque em uma lista P ou I,
conforme os valores forem pares ou ímpares. O tamanho das listas P e I é de 10 posições. Cada vez que
encher uma das listas, (P ou I) esvazie-o, mostrando os valores que estavam na lista. Cada lista P ou I
pode ser preenchido quantas vezes forem necessárias. No final, mostre os valores que restaram em cada
uma das listas.'''

def main():
    p = []
    i = []
    for j in range(30):
        novoValor = int(input(f"Digite o valor {j}: "))
        if novoValor % 2 == 0:
            p.append(novoValor)
            if len(p) == 10:
                for _ in range(10):
                    p.pop()
        else:
            i.append(novoValor)
            if len(i) == 10:
                for _ in range(10):
                    i.pop()

    print(f"Pares: {p}")
    print(f"Impares: {i}")
main()