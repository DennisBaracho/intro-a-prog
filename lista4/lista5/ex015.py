'''Faça um algoritmo que leia um lista V[10] e um lista X[10]. A seguir, crie um lista Y[20] que conterá os valores dos listas V e X em ordem crescente.'''

def ordenar_valores(v, x):
    y = v + x
    y.sort()
    return y


def main():
    v = []
    x = []
    for i in range(10):
        novoV = int(input(f"Digite o valor {(i+1)} de V: "))
        novoX = int(input(f"Digite o valor {(i+1)} de X: "))
        v.append(novoV)
        x.append(novoX)
    y = ordenar_valores(v, x)
    print(y)
main()