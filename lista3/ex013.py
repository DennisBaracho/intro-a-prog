"""Faça um algoritmo que calcula e escreve o valor de S para as equações abaixo:"""

import math

s = 0
numerador = 1
denominador = 1

while(denominador <= 50):
    s += numerador/denominador
    numerador += 2
    denominador += 1
print(f"Para A, o valor de S eh: {s}")

s = 0
expoente = 1
numerador = 2**expoente
denominador = 50

while(expoente != 50):
    s += numerador/denominador
    expoente += 1
    denominador -= 1
print(f"Para B, o valor de S eh: {s}")
