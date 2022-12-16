# Exercício 008 -  Escreva um programa que leia uma medida dada em m e o converta para cm e mm.

medida = float(input('Escreva a comprimento em m: '))
print(f'O comprimento {medida}m convertido para cm fica: {medida*100}cm\nE em mm fica: {medida*1000}mm')