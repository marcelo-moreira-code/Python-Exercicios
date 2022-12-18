# Desafio 028 - Escreva um program que faça o computador 'Pensar' em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint

computador = randint(0,10)

jogador = int(input('Tente adivinhar digitando qual dos números o PC irá jogar de 0 a 10 : '))

if jogador == computador:
    print(f'Você venceu! Pois, vc jogou {jogador} e o PC jogou {computador}')
else:
    print(f'Você Perdeu! O PC jogou {computador} e vc jogou {jogador}')    