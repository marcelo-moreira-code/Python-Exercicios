# Desafio 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número : 6.127
# O número 6.127 tem a parte inteira 6.

num = float(input('Digite um número: '))
print(f'A parte inteira do número {num} é {int(num)}')

# Acho que assim também vale
print(f'{num} é {num:.0f}')

