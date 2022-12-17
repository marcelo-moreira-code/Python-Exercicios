# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import randint
from time import sleep

sorteio = randint(1,4)
alunos = []

for c in range(1,5):
    alunos.append(str(input(f'Informe o nome do {c}º aluno: ')))

print(f'Os alunos que participarão do sorteio são {alunos}')
sleep(2)
print(f'E o aluno sorteado foi -> {alunos[sorteio]}')
