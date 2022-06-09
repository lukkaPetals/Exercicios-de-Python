#-*- coding: utf-8 -*-
n = str(input('Digite seu nome completo')).strip
na = n.split(
print(n)
print('Seu primeiro nome é:{}'.format(na[0]))
print('Seu segundo nome é:{}'.format(na[len(na)-1]))
