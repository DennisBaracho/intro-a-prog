"""Escreva um programa correspondente ao seguinte algoritmo simplificado: 
a. Leia o código de um aluno e suas três notas. 
b. Calcule a média ponderada do aluno com peso 4 para a maior nota, e peso 3 para as 
demais.  
c. Informe o código do aluno, suas três notas, a média calculada e a mensagem  
“APROVADO”, se a média for maior ou igual a 5, ou "REPROVADO", caso contrário. 
d. Repita a operação até que o código lido seja negativo. """

codigoAluno = 1

while codigoAluno > 0:
    codigoAluno = int(input("\nDigite o codigo do aluno: "))
    nota1 = float(input("Digite a primeira nota, de peso 4: "))
    nota2 = float(input("Digite a segunda nota, de peso 3: "))
    nota3 = float(input("Digite a terceira nota, de peso 3: "))

    media = (nota1*4 + nota2*3 + nota3*3)/10

    if media >= 5:
        aprovacao = "APROVADO"
    else:
        aprovacao = "REPROVADO"

    print(f"O aluno {codigoAluno} tem media de {media}, ele esta {aprovacao}")