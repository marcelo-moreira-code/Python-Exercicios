# Exercício 004 - Faça um programa que leia algo na tela e 
# mostre seu tipo primitivo e todas as informações sobre ele.

algo = input('Digite algo: ')
print(f'O tipo primitivo de {algo} é {type(algo)}')
print(f'{algo} é somente números? {algo.isnumeric()}')
print(f'{algo} é formado somente por letras? {algo.isalpha()}')
print(f'{algo} é formado por elementos numéricos ou letras? {algo.isalnum()}') # não entendi .isalnum()
print(f'{algo} escrito em Maiúsculas fica {algo.upper()}')
print(f'{algo} escrito em minúsculas fica {algo.lower()}')
