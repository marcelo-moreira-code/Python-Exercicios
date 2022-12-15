a1 = int(input('Informe o primeiro termo: '))
r = int(input('Razão: '))
n = int(input('Quantos termo squeres exibir: '))
an = a1 + (n-1) * r

for c in range(a1,an+1,r):
    print(c)