"""Escreva um programa que leia 5 valores para uma variável n e, para cada um deles, calcule a 
tabuada de 1 até . Mostre a tabuada na forma:
1 * n = n
2 * n = n
3 * n = n
. . . 
n * n = n²"""

contador = 0

while contador != 5:
    contadorN = 1
    contador += 1 
    n = int(input("Digite a variavel n"))
    while contadorN != n:
        if n > 0:
            resultado = contadorN * n
            print(f"{contadorN} x {n} = {resultado}")
            contadorN += 1
        elif n < 0:
            resultado = contadorN * n
            print(f"{contadorN} x {n} = {resultado}")
            contadorN -= 1
        else:
            print("Digite um valor diferente de zero.")
    

