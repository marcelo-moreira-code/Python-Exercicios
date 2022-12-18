# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez.
# Em que posição ela aparace pela última vez.

frase = str(input('Escreva um frase: ')).strip().upper()
qtd_a = frase.count('A')
posição_inicial_A = frase.find('A')
posição_final_A = frase.rfind('A')
print(f'Na frase {frase} , A vogal A aparece {qtd_a} vezes.')
print(f'E a primeira vez em que ela apareceu foi na posição {posição_inicial_A}')
print(f'A vogal aparece pela última vez na posição {posição_final_A}')
