"""Implemente e teste um programa que leia dois horários no formato hora:minuto e imprima quanto tempo, no formato
hh:mm, se passou entre o primeiro e o segundo horário."""

from datetime import datetime

strHorario1 = input("Digite o horario no formato hh:mm: ")
strHorario2 = input("Digite o horario no formato hh:mm: ")

horario1 = datetime.strptime(strHorario1, '%H:%M')
horario2 = datetime.strptime(strHorario2, '%H:%M')            

tempoDecorrido = (horario2 - horario1)

print(f"Passaram-se {tempoDecorrido}.")