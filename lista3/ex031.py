"""Escrever um algoritmo que lê um conjunto não determinado de valores, um de cada vez, e escreve 
uma tabela com cabeçalho que deve ser repetido a cada 20 linhas. A tabela conterá o valor lido, 
seu quadrado, seu cubo e sua raiz quadrada."""

num = 1
quad = 0
cubo = 0
raiz = 0
linhas = 0

while num != 0:
    num = float(input("Digite um numero (0 para encerrar):"))    
    quad = num*num
    cubo = quad*num
    raiz = num**(1/2)
    if linhas == 0 or linhas % 20 == 0:
        print(f"Quadrado\tCubo\tRaiz\n{quad}\t\t{cubo}\t{raiz}")
    else: 
        print(f"{quad}\t\t{cubo}\t{raiz}") 
    linhas += 1