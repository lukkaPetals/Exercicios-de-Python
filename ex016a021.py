#-*-coding:utf8-*-

'''n = float(input('Digite um numero'))
import math
i = math.floor(n)

print('O numero {} tem a parte inteira {}'.format(n,i))'''

'''c1 = float(input('Digite o primeiro cateto'))
c2 = float(input('Digite o segundo cateto'))
h = c1**2 + c2**2 ** (1/2)
import math
h1 = math.floor(h)
print('O valor da hipótenusa é igual a {:.2f}'.format(h))'''

a1 = (input('Digite o nome de um aluno(a)'))
a2 = (input('Digite o nome de um aluno(a)'))
a3 = (input('Digite o nome de um aluno(a)'))
a4 = (input('Digite o nome de um aluno(a)'))
lista = [a1,a2,a3,a4]

'''import random
s = random.choice(lista)
print('O aluno sorteado foi {}'.format(s))'''


import random
s = random.shuffle(lista)
print('O aluno sorteado foi em ordem:')
print(lista)