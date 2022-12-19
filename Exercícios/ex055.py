# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0

for pessoa in range(1,6):
    peso = int(input(f'Informe o peso da {pessoa}ª pessoa em Kg: '))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso =  peso
print(f'O maior peso foi {maior_peso} Kg')
print(f'E o menor peso foi {menor_peso} Kg')                    
