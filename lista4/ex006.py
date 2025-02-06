'''6. Escreva uma função chamado AUMENTO que receba dois valores reais X e Y como
parâmetros e aumente o valor de X em Y%.
Escreva um algoritmo que leia uma variável K do tipo real e, para um número indeterminado
de funcionários de uma empresa, faça para cada um deles:

Ler a matrícula, o nome e o salário (a leitura da matrícula 0 (zero) indica o fim dos
dados);

Aumente o salário em K% (usando a função AUMENTO) e exiba o salário aumentado.'''

def aumento(x, y):
    x += x*(y/100)
    return x

def main():
    funcionarios = ''
    while (True):
        matricula = int(input("\nDigite a matricula do funcionario: "))
        if matricula == 0:
            print("**Fim da leitura**")
            break
        nome = input("Digite o nome do funcionario: ")
        salario = float(input("Digite o salario do funcionario: "))
        k = float(input("Digite a porcentagem K% que aumentará o salário: "))    
        novoSalario = aumento(salario, k)
        funcionarios += (f"\nMatricula: {matricula} - Nome: {nome} - Salario: R${salario:.2f} - Salario atualizado: R${novoSalario:.2f}.")

    print(funcionarios)

main()