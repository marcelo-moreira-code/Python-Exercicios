# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maiorI = menorI = 0
idade_homem_velho = 0
nome_homem_velho = ''
qtd_mulheres_menoresde20 = 0
soma_idades = 0
for pessoa in range(1,5):
    nome = str(input(f'Informe o nome da {pessoa}ª pessoa: ')).strip().upper()
    idade = int(input(f'A idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Da {pessoa}ª pessoa M/F: ')).upper()
    soma_idades += idade
    if pessoa == 1 and sexo == 'M': # Checando o idade e nome do homem mais velho
        idade = maiorI = idade_homem_velho
        idade = menorI
    else:
        if idade > maiorI:
            maiorI = idade_homem_velho = idade
            nome_homem_velho = nome
        if idade < menorI:
            menorI = idade
    if sexo == 'F' and idade <= 20:
        qtd_mulheres_menoresde20 += 1

          

print(f'A idade do homem mais velho é {idade_homem_velho}, seu nome é {nome_homem_velho}')
print(f'A soma das idades é igual a {soma_idades}, então a média de idade foi de {soma_idades/4:.1f} anos')
print(f'E {qtd_mulheres_menoresde20} mulheres têm menos de 20 anos de idade.')
