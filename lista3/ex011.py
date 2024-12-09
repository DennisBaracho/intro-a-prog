"""Faca um algoritmo que apresente na tela a tabela de conversão de graus Celsius para Fahrenheit
no intervalo de -100 oC a 100 oC com valores igualmente espaçados (5oC em 5oC).
Obs.: Farenheit = (9/5)*(Celsius) + 32."""

celsius = -100
fahrenheit = 0 

print("Celsius \tFahrenheit")
while(celsius <= 100):
    fahrenheit = (9/5)*(celsius) + 32
    print(f"{celsius}\t\t{fahrenheit:.2f}")
    celsius += 1
