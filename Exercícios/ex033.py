#  Desafio 033 - faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''# Fazendo na ignorância
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('O segundo número: '))
num3 = int(input('O terceiro número: '))

# compararando na porrada
if num1 > num2 > num3:
    print(f'O maior número é {num1} e o menor {num3}')
elif num1 > num3 > num2:
    print(f'O maior é {num1} e o menor é {num2}')  
elif num2 > num1 > num3:
    print(f'O maior é {num2} e o menor é {num3}') 
elif num2 > num3 > num1:
    print(f'O maior é {num2} e o menor é {num1}')        
elif num3 > num1 > num2:
    print(f'O maior é {num3} e o menor é {num2}')
elif num3 > num2 > num1:
    print(f'O maior é {num3} e o menor é {num1}')
elif num1 > num2 == num3:
    print(f'O maior é {num1}, mas não há um menor , pois são iguais. {num2} = {num3}')
elif num2 > num1 == num3:
    print(f'O maior é {num2}, mas não há um menor , pois são iguais: {num1} =  {num3}')
elif num3 > num1 == num2:
    print(f'O maior é {num3}, mas não há um menor, pois são iguais : {num1} = {num2}')
elif num1 == num2 > num3:
    print(f'O {num1} = {num2} e são o maior número, já o menor é {num3}')
elif num1 == num3 > num2:
    print(f'Os números {num1} = {num3} são o maior valor. E o menor é {num2}')
elif num2 == num3 > num1:
    print(f'Os números {num2} = {num3} são o maior valor, e o menor é {num1}')            
else:
    print('Todos os números são iguais!')'''


números = []
for c in range(1,4):
    num = int(input(f'Informe o {c}° número: '))
    números.append(num)
print(números)
if max(números) == min(números):
    print(f'Não há um maior nem menor, pois os valore são iguais!')
else:
    print(f'O maior número é {max(números)} e o menor é {min(números)}')                    