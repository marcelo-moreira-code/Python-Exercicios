# Desafio 015 - Faça um programa que pergunte a quantidade de Km percorrido por carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar , sabendo que o carro custa R$ 60 por dia e R$ 0.15 por KM rodado.

dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
distância_percorrida = int(input('Informe quantos Km o carro percorreu no trajeto: Km '))
custo_aluguel = (60 * dias_alugados) + (distância_percorrida * 0.15)

print(f'''O valor a ser pago por um carro alugado por {dias_alugados} dias
E que percorreu {distância_percorrida} km ,
Será de {custo_aluguel} reais.''')