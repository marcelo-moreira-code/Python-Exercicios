# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade (21)# e quantas já são maiores.

from datetime import date
atual = date.today().year
maior_idade = 0
menor_idade = 0
tot_maior = 0
tot_menor = 0
for c in range(1, 8):
    nasceu = int(input(f'Informe o ano de nascimento da {c}° pessoa: '))
    idade = atual - nasceu
    if idade <= 21:
        tot_menor += 1
    else:
        tot_maior += 1
print(f'Há {tot_maior} maiores de idade.')
print(f'E {tot_menor} menores de idade')        
