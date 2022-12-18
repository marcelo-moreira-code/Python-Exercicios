# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Informe seu nome completo: ')).strip().upper()
if 'SILVA' in nome:
    print(f'No nome {nome} , há SILVA.')
else:
    print('Não há SILVA nesse nome!')    
