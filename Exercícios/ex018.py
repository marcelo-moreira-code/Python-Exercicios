# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'''Para o ângulo {ângulo}°, temos :
seno = {seno:.1f}
cosseno = {cosseno:.1f}
tangente = {tangente:.1f}''')
