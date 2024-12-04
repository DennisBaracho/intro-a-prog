"""Uma empresa deseja dar aos seus funcionários um abono de salário de acordo com a sua
produtividade. Sabe-se que a empresa divide os seus funcionários nas seguintes categorias de
acordo com o seu desempenho:
. Ótimo (categoria 1) - 20% de abono
. Bom (categoria 2) - 15% de abono
. Regular (categoria 3) - nenhum abono
Implemente e teste um programa que leia o salário de um funcionário e a sua categoria de
abono(inteiro) e imprima o salário total."""

salario = float(input("Digite o seu salario: R$"))
categoria = int(input(f"\nDigite sua categoria de abono: \n1. Ótimo - 20% de abono\n2. Bom - 15% de abono.\n3. Regular - nenhum abono.\n"))
salarioTotal = 0

if(categoria != 1) and (categoria != 2) and (categoria != 3):
    print("Digite uma categoria de 1 a 3.")
else:
    if(categoria == 1):
        salarioTotal = salario*120/100
    elif(categoria == 2):
        salarioTotal = salario*115/100
    else:
        salarioTotal = salario
    print(f"Seu salario total: {salarioTotal}")