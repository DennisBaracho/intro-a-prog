"""Foi feita uma pesquisa entre os habitantes de uma regiC#o. Foram coletados os dados de idade,
sexo (M ou F) e salario. Faca um algoritmo que informe:
a. A media de salario do grupo;
b. Maior e menor idade do grupo;
c. Quantidade de mulheres com salario ate) R$1000,00."""

idade = 1
sexo = 0
maiorIdade = 0
menorIdade = 0
fAte1000 = 0
mediaSalario = 0
pessoas = 0

while idade > 0:
    idade = int(input("Digite a idade do morador: "))
    if idade > 0:
        sexo = input("Digite o sexo (M) - masculino ou (F) - feminino: ")
        salario = float(input("Digite o salario do morador: "))
        mediaSalario += salario
        if idade > maiorIdade:
            maiorIdade = idade
        elif idade < menorIdade:
            menorIdade = idade
        if sexo == "F":
            fAte1000 += 1
        pessoas += 1

mediaSalario /= pessoas
print(
    f"A media de salario do grupo eh: {mediaSalario}\nA maior idade eh: {maiorIdade}\nA menor idade eh: {menorIdade}\nO numero de mulheres com salario ate 1000 reais eh: {fAte1000}"
)
