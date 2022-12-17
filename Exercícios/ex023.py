# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número : 1834
# Unidade: 4
# Dezena : 3
# Centena: 8
# Milhar : 1

num = int(input('Escreva um número que esteja no intervalo de 0 a 9999: '))
unid = num%10
deze = num%100
cent = num%1000
milh = num%10000

print(f'Para o número {num} temos : ')
print(f'Unidade: {unid}')
print(f'Dezenda: {(deze-unid)//10}')
print(f'Centena: {(cent-deze)//100}')
print(f'Milhar: {(milh-cent)//1000}')

