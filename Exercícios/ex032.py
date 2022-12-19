# Desafio 032 - Faça um programa que leia um ano qualquer e e mostre se ele  é bissexto.

from datetime import date
atual = date.today().year
print(atual)

ano = int(input('Informe o ano a ser analisado: '))
if (ano % 4 == 0 and ano % 100 != 0) or  (ano % 4 == 0 and ano % 400 == 0) :
    print('É ano Bissexto!')
else:
    print('Não é ano Bissexto!')    