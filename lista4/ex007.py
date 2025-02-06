'''7. Escreva um algoritmo que leia as 3 notas e o número de faltas de um aluno, calcule a sua
média e determine e exiba a sua situação. Caso a aluno tenha mais de 18 faltas, ele está
REPROVADO POR FALTA. Caso contrário, estará REPROVADO se sua média for menor
que 6.0 ou APROVADO se sua média for superior a 6.0.
Observações:

Disciplina: Programação Estruturada / Programação II

Utilize uma função para calcular a média e uma função para determinar e exibir a
situação do aluno;'''

def media(s):
    m = (s)/3
    return m

def situacao(f, m):
    if f > 18 or m < 6:
        s = "REPROVADO"
    else:
        s = "APROVADO"
    print(f"O aluno esta {s}! Media: {round(m,2)} - Faltas: {f}.")

def main():
    soma = 0
    mediaNotas = 0
    i = 1
    notas = 0
    while i <= 3:
        notas = float(input(f"Digite a nota {i}: "))
        soma += notas
        i += 1
    mediaNotas = media(soma)
    faltas = int(input("Digite o numero de faltas do aluno: "))
    situacao(faltas, mediaNotas)
main()
    
    