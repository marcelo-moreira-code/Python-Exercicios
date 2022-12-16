# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto  e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Quanto mede o cateto oposto: '))
cateto_adjacente = float(input('E cateto adjacente: '))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)
print(f'A hipotenusa de um triângulo com os catetos oposto {cateto_oposto}, e o adjacente {cateto_adjacente} é {hipotenusa}')

# Ou 

'''from math import hypot
h = hypot(cateto_oposto,cateto_adjacente)
print(h)'''