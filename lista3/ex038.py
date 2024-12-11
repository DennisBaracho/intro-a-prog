"""Escreva um programa que leia um conjunto de 50 informações contendo, cada uma delas, a altura 
e o sexo de uma pessoa (M) - masculino ou (F) - feminino), calcule e mostre o seguinte: 
a. A maior e a menor altura da turma; 
b. A média da altura das mulheres. 
c. A média da altura da turma."""

contador = 0
masculino = 0
feminino = 0
sexo = 0
altura = 0 
mediaAltFem = 0
mediaAltGeral = 0
menorAlt = 0
maiorAlt = 0

while contador < 3:
    altura = float(input("Digite a altura da pessoa: "))
    if contador == 0:
        maiorAlt = altura
        menorAlt = altura
    sexo = input("Digite o sexo da pessoa 'M' para masculino e 'F' para feminino: ")
    if sexo == 'M':
        masculino += 1
        mediaAltGeral += altura
    elif sexo == 'F':
        feminino += 1
        mediaAltFem += altura
        mediaAltGeral += altura
    if altura > maiorAlt:
        maiorAlt = altura
    elif altura < menorAlt:
        menorAlt = altura
    contador += 1
    
mediaAltFem /= feminino
mediaAltGeral /= (feminino + masculino)
print(f"\nMaior altura da turma: {maiorAlt}\nMenor altura da turma: {menorAlt}\nMedia de altura das mulheres: {round(mediaAltFem,2)}\nMedia de altura da turma: {round(mediaAltGeral,2)}")

