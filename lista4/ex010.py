'''10. Escreva uma função chamada DIAS_ANO que receba 3 valores inteiros (DIA, MES, ANO)
e retorne o número de dias decorridos no ano até o dia/mês/ano fornecido.
Escreva uma função com retorno booleano chamada DATA_VALIDA que receba uma data
(DIA, MÊS, ANO) e verifique se a data é válida (considerando os anos bissextos).
Faça um algoritmo que leia 2 datas, no formato dia, mês e ano (as datas devem ter o mesmo
ano) verificando se elas são válidas (através da função DATA_VALIDA), calcule e exiba a
diferença de dias entre elas (usando a função DIAS_ANO).'''

def dias_ano(d, m, a):
    totalDias = d
    i = 0

    if (a % 4 == 0):
        anoBissexto = True
    else:
        anoBissexto = False

    while i < m:
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            totalDias += 31
        elif i == 2:
            if anoBissexto == True:
                totalDias += 29
            else:
                totalDias += 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            totalDias += 30
        i += 1
    
    return totalDias

def data_valida(d, m, a):
    return None

def main():
    dia1, mes1, ano1 = (input("Digite dia, mes e ano da primeira data: ")).split()
    diasData1 = dias_ano(int(dia1), int(mes1), int(ano1))
    dia2, mes2, ano2 = (input("Digite dia, mes e ano da primeira data: ")).split()
    diasData2 = dias_ano(int(dia2), int(mes2), int(ano2))
    diasEntre = diasData2 - diasData1
    print(f"Dias entre {dia1}/{mes1}/{ano1} e {dia2}/{mes2}/{ano2}: {diasEntre}")

main()