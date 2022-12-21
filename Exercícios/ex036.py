# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa , o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Informe o valor da casa em: R$ '))
salário_comprador = float(input('Quanto ganha mensalmente? R$ '))
tempo_pag = float(input('Em quantos anos queres pagar a casa: '))
prestação_mensal = valor_da_casa / (tempo_pag * 12) 
print(f'{prestação_mensal:.1f}')
if prestação_mensal > (salário_comprador * 0.3):
    print('Empréstiomo Recusado! Pois, a prestação mensal não pode exceder 30% do salário do credor.')
else:
    print('Seu empréstimo foi aprovado! Meus parabêns!')    