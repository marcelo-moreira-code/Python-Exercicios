# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número : 1834
# Unidade: 4
# Dezena : 3
# Centena: 8
# Milhar : 1

num = int(input('Escreva um número que esteja no intervalo de 0 a 9999: '))

print(f'Unidade: {num[0]}')
print(f'Dezena: {num:.1f}')
print(f'Centena: {num:.2f}')
print(f'Milhar: {num:.3f}')
