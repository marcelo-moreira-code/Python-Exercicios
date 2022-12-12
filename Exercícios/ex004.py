# Exercício 004 - Faça um programa que leia algo na tela e 
# mostre seu tipo primitivo e todas as informações sobre ele.

algo = input('Digite algo: ')
print(f'O tipo primitivo de {algo} é {type(algo)}')
print(f'{algo} é numérico? {algo.isnumeric}')
print(f'{algo} é formado somente por letras? {algo.isalpha}')
print(f'{algo} é formado por elementos numéricos e letras? {algo.isalnum}')
