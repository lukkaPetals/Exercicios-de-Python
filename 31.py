#-*- coding: utf-8 -*-
d = int(input('Qual a distância da sua viagem?:km'))
if d <= 200:
	d * 0.50
	print('O preço de sua viagem é R${}'.format(d))
else:
	d * 0.45
	print('O preço de sua viagem é R${}'.format(d))