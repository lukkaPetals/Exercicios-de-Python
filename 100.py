from math import radians
from random import randint
números = []

def sorteia():
    for c in range(1,6):
        números.append(randint(1,999))
    print(f'Os números sorteados foram {números}')

def somapar():
    soma = 0
    for d in números:
        if d % 2 == 0:
            soma += d
    if soma == 0:
            print('Não houveram números pares')
    print(f'A soma dos números pares foi {soma}')


sorteia()
somapar()
