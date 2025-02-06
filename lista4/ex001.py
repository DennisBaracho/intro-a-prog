'''1. Escreva uma função chamada CUBO que receba um valor do tipo real e retorne a potência
elevado a 3 do mesmo.'''


def cubo(a):
    return pow(a,3)

def main():
    valor = float(input("Digite um valor real: "))
    potencia = (cubo(valor))
    print(f"Cubo: {potencia}")

main()
