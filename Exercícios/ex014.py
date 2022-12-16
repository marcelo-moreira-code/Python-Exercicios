# Desafio 014 - Faça um programa que converta uma temperatura digitada em C° para F°.

# tc/5 = (tf-32)/9 -> tf = (tc/5) * 9 + 32

temperatura_celcius = float(input('Informe a temperatura em C°: '))
temperatura_farheirait = (temperatura_celcius * 9)/5 + 32

print(f'\033[34m{temperatura_celcius} C°\033[m convertido para Farheirait fica \033[31m{temperatura_farheirait} F°\033[m')
