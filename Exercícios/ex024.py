# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'.

cidade = str(input('Escreva o nome da cidade: ')).strip().upper()
separa_cidade = cidade.split()
if 'SANTO' in separa_cidade[0]:
    print('Sim, esta cidade começa com SANTO.')
else:
    print('Não começa!')     