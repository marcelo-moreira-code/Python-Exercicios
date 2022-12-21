# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# minha solução sofrida
'''números_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze'
,'dezesseis','dezessete','dezoito','dezenove','vinte')

print(len(números_extenso))
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num >= 21:
        print('Número Inválido!')
        continue
    if num >= 0 and num <= 21:
        for c in range(0,22):
                if c >= 0 and c <= 21:
                    if num == c:
                        print(f'O número {num}, por extenso fica -> {números_extenso[num]}')
                        break
    break'''
            

# testando

'''for index, num in enumerate(números_extenso):
    # print(f'{index} , {num} ')
    núm = int(input('Digite um número entre 0 e 20: '))
    if index == 0:
        if núm == index:
            print(f'o número {núm} por extenso fica {números_extenso[index]}')'''

'''# Solução do professor Guanabara

cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze'
,'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!', end=' ')
print(f'Você digitou o número {cont[num]}')'''


