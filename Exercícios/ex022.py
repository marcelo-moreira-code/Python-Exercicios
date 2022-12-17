# Desafio 022 -Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo: ')).strip()
nome_separado = nome.split()
primeiro_nome = nome_separado[0]
nome_sem_esp = nome.replace(' ','')

print(f'''O seu nome em maiúsculas fica : {nome.upper()}
Em minúsculas fica : {nome.lower()}
No total, seu nome tem : {len(nome)} letras.
Sem espaços fica com : {len(nome_sem_esp)} letras.
E seu primeiro nome é : {primeiro_nome} e tem {len(primeiro_nome)} letras.''')