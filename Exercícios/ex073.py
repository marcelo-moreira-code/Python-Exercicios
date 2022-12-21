# Desafio 073 - Crie uma tupla que mostre os 20 primeiros times do campeonato brasileiro de futebol da séria A,na ordem de colocação.
# Depois mostre:
# 1 - Os 5 primeiros times
# 2 - Os últimos 4 times
# 3 - Times em ordem alfabética
# Em que posição está o time do São Paulo

'''CLASSIFICAÇÃO
1º Palmeiras
2ºInternacional
3º Fluminense
4º Corinthians
5º Flamengo
6º Athletico-PR
7º Atlético-MG
8º Fortaleza
9º São Paulo
10º América-MG
11º Botafogo
12º Santos
13º Goiás
14º Bragantino
15º Coritiba
16º Cuiabá
17º Ceará
18º Atlético-GO
19º Avaí
20º Juventude'''

times = ('1º Palmeiras','2ºInternacional','3º Fluminense','4º Corinthians','5º Flamengo','6º Athletico-PR','7º Atlético-MG','8º Fortaleza','9º São Paulo',
'10º América-MG','11º Botafogo','12º Santos','13º Goiás','14º Bragantino','15º Coritiba','16º Cuiabá','17º Ceará','18º Atlético-GO','19º Avaí','20º Juventude')
print(len(times))
print(f'O 5 primeiros colocados são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[16:21]}')
print(f'E a posição do São Paulo é {times.index(8)}')
