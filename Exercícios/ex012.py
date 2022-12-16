# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

preço_atual = float(input('Informe o preço do produto: '))
preço_desconto = preço_atual * 0.95
print(f'O preço do produto custa R$ {preço_atual} , mas já que você possui um cupom de desconto de 5%,\nEle vai sair a R$ {preço_desconto}')
print('Muito obrigado pela sua preferência, Volte sempre!')