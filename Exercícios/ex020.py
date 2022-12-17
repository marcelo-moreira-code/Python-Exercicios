# Desafio 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um progama que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
lista_nomes = []
for nome in range(1,5):
    lista_nomes.append(str(input(f'Informe o nome do {nome}ª aluno: ')))

print(lista_nomes)


random.shuffle(lista_nomes)
print(lista_nomes)