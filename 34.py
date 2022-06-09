#-*- coding: utf-8 -*-
s = int(input('digite seu salário atual'))
if s > 1250:
	a = (s * 0.10) + s
else:
	a = (s * 0.15) + s
print('O seu salário atual é R${:.2f}'.format(a))