# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de  tinta necessária para pintá-la,sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Agoro, a altura da parede:  '))
área = largura * altura
qtd_litros = área / 2
print(f'Uma parede que possua uma altura de {altura}m , e uma largura  de {largura}m ')
print(f'Resultando numa área de {área}m², necessita de {qtd_litros} litros de tinta para pintá-la.')