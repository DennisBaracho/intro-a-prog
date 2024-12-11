"""A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o
salário e número de filhos. A prefeitura deseja saber:
a. Média do salário da população.
b. Média do número de filhos.
c. Maior salário.
d. Percentual de pessoas com salário até R$100,00.
O final da leitura de dados se dará com a entrada de um salário negativo."""

salario  = float(input("Digite seu salário. Digite um salário negativo para encerrar."))
mediaSalario = 0 
mediaFilhos = 0
qtdEntrevistados = 0
maiorSalario = salario 
baixoSalario = 0

if salario >= 0:
    filhos = int(input("Digite quantos filhos voce tem: "))
    if salario <= 100:
        baixoSalario += 1
    if salario > maiorSalario:
        maiorSalario = salario
    mediaSalario += salario
    mediaFilhos += filhos
    qtdEntrevistados += 1

while(salario >= 0):
    salario  = float(input("Digite seu salário. Digite um salário negativo para encerrar."))   
    if salario > 0:
        filhos = int(input("Digite quantos filhos voce tem: "))
        if salario <= 100:
            baixoSalario += 1
        if salario > maiorSalario:
            maiorSalario = salario
        mediaSalario += salario
        mediaFilhos += filhos
        qtdEntrevistados += 1

mediaSalario /= qtdEntrevistados
mediaFilhos /= qtdEntrevistados

print(f"\nA media de filhos da populacao eh: {mediaFilhos}")
print(f"A media de salario da populacao eh: R${mediaSalario}")
print(f"O percentual de pessoas com salario ate R$100.00 eh de: {(baixoSalario*100)/qtdEntrevistados}%")
print(f"O maior salario eh de R${maiorSalario}")