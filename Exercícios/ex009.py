# Exercício 009 - Crie um programa que peça na tela um número inteiro qualquer e mostre na tela sua tabuada.

num = int(input('Digite um número para ter sua tabuada: '))
"""
print(f'{num} x {0} = {num*0}')
print(f'{num} x {1} = {num*1}')
print(f'{num} x {2} = {num*2}')
print(f'{num} x {3} = {num*3}')
print(f'{num} x {4} = {num*4}')
print(f'{num} x {5} = {num*5}')
print(f'{num} x {6} = {num*6}')
print(f'{num} x {7} = {num*7}')
print(f'{num} x {8} = {num*8}')
print(f'{num} x {9} = {num*9}')
print(f"{num} x {10} = {num*10}")
"""

# com laço for
print('<->'*20)
for c in range(0,11):
    print(f'{num} x {c} = {num*c}')

