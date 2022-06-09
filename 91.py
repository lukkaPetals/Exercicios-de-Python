from random import randint
from operator import itemgetter

jogadas = {}
for c in range(1, 5):
    jogadas[f'Jogador{c}'] = randint(1,6)
ranking = {}
for k, v in jogadas.items():
    print(f'O {k} tirou {v}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(ranking)
