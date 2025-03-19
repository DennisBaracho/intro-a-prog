'''9. Escreva uma função chamada NOME_MES que receba um valor inteiro N (de 1 a 12) e
retorne uma cadeia de caracteres (texto) contendo o nome do mês correspondente a N.
Faça um algoritmo que leia uma data (no formato dia, mês e ano) e, usando a função
NOME_MES, exiba a data lida no formato abaixo:
EXEMPLO: Entrada: 23 11 1998 Saída: 23 de novembro de 1998'''

def nome_mes(n):

    if n == 1:
        mesTexto = "Janeiro"
    elif n == 2:
        mesTexto = "Fevereiro"
    elif n == 3:
        mesTexto = "Marco"
    elif n == 4:
        mesTexto = "Abril"
    elif n == 5:
        mesTexto = "Maio"
    elif n == 6:
        mesTexto = "Junho"
    elif n == 7:
        mesTexto = "Julho"
    elif n == 8:
        mesTexto = "Agosto"
    elif n == 9:
        mesTexto = "Setembro"
    elif n == 10:
        mesTexto = "Outubro"
    elif n == 11:
        mesTexto = "Novembro"
    else:
        mesTexto = "Dezembro"
    return mesTexto 

def main():
    dia, n, ano= (input("Digite a data em numeros: ")).split()
    dia = int(dia)
    n = int(n)
    ano = int(ano)
    mes = nome_mes(n)
    print(f"{dia} {mes} {ano}")

main()