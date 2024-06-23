# Exercício 041: A Conferência Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: #
# - Até 9  anos :       MIRIM
# - Até 14 anos :        INFANTIL
# - Até 19 anos :        JÙNIOR
# - Até 25 anos :        SENIOR
# - Acima de 25 anos:   MASTER

nome = str(input("Digite seu nome completo: ")).upper()
nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2024 - nascimento

print(f"Olá {nome}, sua idade é {idade} anos. E você está na categoria: ")
if idade == 9:
    print("MIRIM!")
elif idade == 14:
    print("INFANTIL!")
elif idade == 19:
    print("JÙNIOR!")
elif idade == 25:
    print("SENIOR!")
else:
    print("MASTER!")
    