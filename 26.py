#-*- coding: utf-8 -*-

f = str(input('Digite uma frase qualquer')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(f.count('a')))
print('A letra A apareceu pela primeira vez na posição {}'.format(f.find('a')+1))
print('A letra A apareceu pela primeira vez na posição {}'.format(f.rfind('a')+1))
