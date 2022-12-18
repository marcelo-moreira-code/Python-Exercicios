# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da  passagem ,
# cobrando R$ 0.50 por Km  para viagens de até 200Km  e R$ 0.45 para viagens mais longas.

distância = int(input('Qual foi a distância (em KM) percorrida pelo veículo na viagem: '))
if distância <= 200:
    print(f'Preço da passagem é de R$ {distância * 0.5}')
else:
    print(f'Preço da passagem é de R$ {distância * 0.45}')    