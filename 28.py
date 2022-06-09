#-*- coding: utf-8 -*-
from random import randint
pc = randint(0, 5)
print('pensei em um número entre 0 e 5')
h = int(input('Tente advinhar'))
if pc == h:
	print('Parabéns! Você acertou!')
else:
	print('ERROU! eu pensei no número {}'.format(pc))