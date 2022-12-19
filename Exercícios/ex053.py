# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Escreva um frase: ')).strip().upper()
frase_sem_espaço = frase.replace(' ', '')
frase_invertida_sem_espaço = frase_sem_espaço[::-1]
print(frase_sem_espaço)
print('+-+' * 15)
print(frase_invertida_sem_espaço)

if frase_sem_espaço == frase_invertida_sem_espaço:
    print('É Palindromo!')
    print(f'Pois, a frase: {frase_sem_espaço}')
    print(f'É igual ao seu inverso : {frase_invertida_sem_espaço}')
else:
    print('Não é Palíndromo!')    

