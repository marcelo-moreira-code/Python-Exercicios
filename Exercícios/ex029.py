# Desafio 029 - Escreva um programa que leia a velocidade de carro, Se ele ultrapassar 80km/h , mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada Km  acima  do limite.

vel_carro = int(input('Informe a velocidade do carro durante o trajeto: '))
multa = (vel_carro - 80) * 7
if vel_carro > 80:
    print('Você foi multado por excesso de velocidade!')
    print(f'O valor da multa é de R$ {multa}')
else:
    print('Sua velocidade está correta. Tenha uma boa tarde!')    