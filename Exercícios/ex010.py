# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerando U$ 1,00 = R$ 3,27r.    

dinheiro_em_reais = float(input('Informe quantos reias você tem na carteira: R$  '))
dinheiro_em_dólares = dinheiro_em_reais / 3.27
print(f'Com R$ {dinheiro_em_reais} , você consegue comprar ${dinheiro_em_dólares}')

