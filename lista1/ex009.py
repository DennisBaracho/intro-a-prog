"""Implemente e teste um programa que leia dois valores inteiros representando, respectivamente, um valor de hora e um
de minutos e imprima o valor equivalente em minutos. Por exemplo: Digite o numero de horas e o numero de minutos: 9 15
Tempo decorrido: 555 minutos."""

hora, min = (input("Digite dois valores inteiros: ")).split()
tempoDecorrido = (int(hora)*60) + int(min)

print(f"Tempo decorrido: {tempoDecorrido} minutos.")