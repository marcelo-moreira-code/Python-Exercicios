# Desafio 034- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais , o aumento é de 15%.

salário = float(input('Informe o salário: R$ '))
if salário >= 1250:
    print(f'''Parabêns, você recebeu um aumento de 10% no seu salário!
    Seu antigo salário era de R${salário} , e agoro é R$ {salário*1.10}''')
else:
    print(f'''Parabêns, você recebeu um aumento de 15%no seu salário!
    Ele era de R$ {salário} , e com o aumento ficou R$ {salário*1.15}''')