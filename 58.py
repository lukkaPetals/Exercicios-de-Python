#-*- coding: utf-8 -*-
from random import randint
pc = randint(0, 10)

print('pensei em um número entre 0 e 10: ')
print('Tente acertar ele')
a = False
while not a:
    j = int(input('Qual seu chute?: '))
    if j == pc:
        a = True
print('Boa mlk')