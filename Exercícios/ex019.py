# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import randint

aluno1 = input('Informe o(a) nome do(a) aluno(a): ')
aluno2 = input('Informe o(a) nome do(a) aluno(a): ')
aluno3 = input('Informe o(a) nome do(a) aluno(a): ')
aluno4 = input('Informe o(a) nome do(a) aluno(a): ')

sorteio = randint(1, 4)


