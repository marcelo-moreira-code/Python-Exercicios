# Desafio 013- Faça um programa que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento.

salário_atual = float(input('Informe o salário do funcionário: R$  '))
salário_reajustado = salário_atual * 1.15
print(f'''Meus parabêns, Você conseguiu uma promoção ! 
Com isso, seu salário que era de R$ {salário_atual} 
Passa a ser de R$ {salário_reajustado}''')
