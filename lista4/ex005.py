'''5. Escreva uma função chamada MEDIA que retorne a média de 3 valores reais (X, Y e Z)
passados como parâmetros.
Escreva um algoritmo que, para um número indeterminado de alunos, faça para cada um
deles:
Ler o nome e as 3 notas do aluno (a leitura do nome “FIM” indica o fim dos dados);
Calcule a média do aluno (usando a função MEDIA);
Exiba o nome e a média do aluno.'''

def media(x, y, z):
    m = (x + y + z)/3
    return m

def main():
    resultadoFinal = ''
    nomeAluno = ''
    while (nomeAluno != "FIM"):
        nomeAluno = ''
        nomeAluno = input("Digite o nome do aluno. Para finalizar, digite 'FIM': ")
        if nomeAluno == "FIM":
            break
        nota1, nota2, nota3 =  (input("Digite as 3 notas do aluno em uma linha: ")).split()
        mediaAluno = media(float(nota1), float(nota2), float(nota3))
        resultadosAlunos = (f"Nome do aluno: {nomeAluno} - Media: {mediaAluno}.\n")
        resultadoFinal += resultadosAlunos
    print(resultadoFinal)

main()