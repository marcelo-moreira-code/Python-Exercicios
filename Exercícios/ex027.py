# Desafio 027 - Faça um program que leia o nome completo de uma pessoa, mostrando  em seguida
# o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Informe seu nome completo: ')).strip().upper()
separado = nome.split()
primeiro_nome = separado[0]
último_nome = separado[-1]

print(f'''O seu nome completo é {nome}
E seu primeiro nome é {primeiro_nome}
Já o seu último nome é {último_nome}''')