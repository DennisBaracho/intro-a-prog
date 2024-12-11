"""Faça um programa que calcule o valor do cosseno de (em radianos) através de 40 termos da
série abaixo:"""

a = int(input("Digite o valor de a: "))
cont = 0 
soma = 0
termo = 2
fatorial = 1 
contFatorial = 1 

while(cont < 40):
    fatorial = 1 
    contFatorial = termo
    while contFatorial >= 1:
        fatorial *= contFatorial 
        contFatorial -= 1
    if cont % 2 == 0:
        soma -= (a**termo)/fatorial 
    else:
        soma += (a**termo)/fatorial 
    cont += 1 
    termo += 2 
    
print(f"O valor do cosseno de a (em radianos) eh {1-soma}")
