## Exercício 043: Desenvolva uma lógica que leia o peso de a latura de uma pessoa, calcule 
# seu Índice de Massa Corporal(IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - Entre 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbita

nome = str(input("Digite seu primeiro nome: "))
peso = float(input("Digite seu peso em kg: "))
altura = float(input(("Digite sua altura em metros: ")))
imc = peso/(altura)**2

print(f"Olá {nome}, seu Índice de Massa Corporal deu: {imc:.2f}")
print("é um IMC de Peso Ideal!")