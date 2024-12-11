"""Escreva um algoritmo que leia 5 pares de valores (a,b) , todos inteiros e positivos, um par de cada vez, e com a < b , escreve os inteiros pares de a até b, incluindo a e b se forem pares.""" 

contador = 0

while contador != 5:
    a, b = (input("\nDigite dois valores inteiros, a < b: ")).split()
    a = int(a)
    b = int(b)
    print(f"Numeros pares entre {a} e {b}:", end = " ")
    if(a == b) or (a > b):
        print("Digite dois valores diferentes em que a seja menor que b")
        contador -= 1
    elif(a % 2 == 0) and (b % 2 == 0):
        while a <= b:
            if a % 2 == 0:
                print(a, end = " ")
            a += 1
    elif(a % 2 == 0) and (b % 2 != 0):
        while a < b:
            if a % 2 == 0:
                print(a, end = " ")
            a += 1 
    else:
        while a < b:
            a += 1
            if a % 2 == 0:
                print(a, end = " ")
    contador += 1

