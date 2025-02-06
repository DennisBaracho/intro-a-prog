'''8. Escreva uma função chamada SEG para receber uma medida de tempo expressa em
horas, minutos e segundos e retornar esta medida convertida apenas para segundos.
Escreva uma função chamado HMS para receber uma medida de tempo expressa apenas em
segundos e retornar esta medida convertida para horas, minutos e segundos.
Faça um algoritmo que leia 2 medidas de tempo (expressas em horas, minutos e segundos)
e, usando a função SEG e o função HMS, calcule e exiba a diferença (também em horas,
minutos e segundos) entre elas.'''

def seg(h, m, s):
    segundos = (h*3600) + (m*60) + (s)
    return segundos

def hms(s):
    horario = (f"{s // 3600}h " + f"{(s % 3600)//60}m " + f"{s % 60}s ")
    return horario
    
def main():
    horas1, minutos1, segundos1 = input("Digite horas, minutos e segundos na mesma linha: ").split()
    horas2, minutos2, segundos2 = input("Digite horas, minutos e segundos na mesma linha: ").split()
    horario1 = seg(int(horas1), int(minutos1), int(segundos1))
    horario2 = seg(int(horas2), int(minutos2), int(segundos2))
    diferenca = hms(abs(horario1 - horario2))
    print(f"A diferença é de: {diferenca}")
main()
    