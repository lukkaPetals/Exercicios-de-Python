#-*- coding: utf-8 -*-
r1 = int(input('digite o primeiro valor'))
r2 = int(input('digite o segundo valor'))
r3 = int(input('digite o terceiro valor'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Seus valores conseguem formar um triângulo')
else:
	print('Seus valores não conseguem formar um triângulo')