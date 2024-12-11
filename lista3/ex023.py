"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de
códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
1, 2, 3 e 4: Voto para os respectivos candidatos
5: Voto nulo
6: Voto em branco
Elabore um algoritmo que leia diversos códigos (até que o código 0 seja digitado) e mostre a
seguinte estatística:
a. Total de votos para cada candidato.
b. Total de votos nulos.
c. Total de votos em branco."""

voto = 1
votosMoacir = 0
votosJoana = 0
votosPedrinho = 0
votosVitoria = 0
votosNulos = 0
votosBrancos = 0

while(voto != 0):
    voto = int(input("Digite para quem vai o seu voto:\n1. Pedrinho\n2. Moacir\n3. Joana\n4. Vitoria\n5. Voto nulo\n6. Voto em branco\n0. Para encerrar\n"))
    if(voto == 1):
        votosPedrinho += 1
    elif(voto == 2):
        votosMoacir += 1
    elif(voto == 3):
        votosJoana += 1
    elif(voto == 4):
        votosVitoria += 1
    elif(voto == 5):
        votosNulos += 1
    elif(voto == 6):
        votosBrancos += 1

print(f"\nVotos para Pedrinho: {votosPedrinho}\nVotos para Moacir: {votosMoacir}\nVotos para Joana: {votosJoana}\nVotos para Vitoria: {votosVitoria}\nVotos nulos: {votosNulos}\nVotos em branco?: {votosBrancos}")