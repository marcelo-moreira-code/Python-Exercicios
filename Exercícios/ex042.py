# Exercício 042: Refaça o Desafio 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados são diferentes

print("Testando se três seguimentos de reta formam ou não um triângulo: ")
lado1 = float(input('Digite o primeiro seguimento : '))
lado2 = float(input("Digite segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

""" Lei de formação dos triângulos
 (l1 + l2) > l3 or (l2 + l3) > l1 or (l1 + l3) > l2
  (3 + 4) > 5       (4 + 5) > 3           (3 + 5) > 4
"""

if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    print("Pode formar um triângulo!")
    if (lado1 == lado2 == lado3):
        print("O triângulo formado é EQUILÁTERO!")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("O triângulo formado é ISÓSCELES!")
    else:
        print("O triângulo formado é ESCALENO!")
else:
    print("Infelizmente não podem formar um triângulo!")
