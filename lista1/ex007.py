"""Implemente e teste um programa que leia as coordenadas de dois pontos e calcule a distância Manhattan. A distância
Manhattan é dada por: d = |x1 − x2| + |y1 − y2|"""

x1 = int(input("Digite a coordenada X do primeiro ponto: "))
y1 = int(input("Digite a coordenada Y do primeiro ponto: "))

x2 = int(input("Digite a coordenada X do segundo ponto: "))
y2 = int(input("Digite a coordenada Y do segundo ponto: "))

distancia = abs((x1 - x2)) + abs((y1 - y2))
print(f"A distancia Manhattan entre os pontos eh: {distancia}")