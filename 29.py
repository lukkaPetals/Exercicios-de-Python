#-*- coding: utf-8 -*-
v = int(input('Qual foi a velocidade registrada pelo radar?:'))
if v > 80:
	print('ATENÇÃO! VOCÊ FOI MULTADO(A)!')
	m = (v - 80)* 7
	print('Sua velocidade estava em {}km/h e por isso você foi multado em R${}'.format(v, m))
else:
	print('Você está dentro do limite ')