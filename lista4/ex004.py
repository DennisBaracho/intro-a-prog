'''4. Escreva uma função chamado METADE que divida um valor do tipo real (passado como
parâmetro) pela metade. Escreva um algoritmo que leia um vetor A de 30 elementos reais e, usando a função METADE,
divida todos seus elementos pela metade.'''

def metade(n):
    m = n/2
    return m

def main():
    valores = []
    resultado = []
    resultados = ''
    nElementos = 0
    while (nElementos < 30):
        valor = float(input("Digite um valor real: "))
        valores.append(valor)
        resultado = metade(valor)
        resultados += (f"\nA metade de {valores[nElementos]} eh igual a {resultado}.")
        nElementos += 1
    
    print(resultados)

main()