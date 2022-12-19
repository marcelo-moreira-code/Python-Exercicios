# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

#nota 
'''Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e
menor que a soma dos outros dois lados.'''

r1 = float(input('Digite o valor do comprimento da primeira reta : '))
r2 = float(input('Digite o valor do comprimento da segunda reta : '))
r3 = float(input('Digite o valor do comprimendo da terceira reta : '))
if r1 > (r2-r3) and r1 > (r3-r2) and r2 > (r1-r3) and r2 > (r3-r1) and r3 > (r1-r2) and r3 > (r2-r1):
    print(f'Com os comprimentos {r1},{r2} e {r3} é possível formar um triângulo.')
else:
    print(f'Com  os comprimentos {r1},{r2} e {r3} não é possível formar um triângulo.')