from random import sample
from time import sleep
jogos = []
n = int(input('Quantos jogos?: '))
for j in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a)
    print(f'Jogo {j+1}: {a}')
    sleep(0.5)
