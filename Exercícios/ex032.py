# Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto ou não.

# Para ser ano bissexto têm que ser : divisível por 4 e não divisível por 100 ; (mas , tem de ser divisível por 400?) 

ano = int(input('Informe o ano a ser analisado: '))

if (ano % 4 == 0 and ano % 100 != 0) or  (ano % 4 == 0 and ano % 400 == 0) :
    print('É ano Bissexto!')
else:
    print('Não é ano Bissexto!')    