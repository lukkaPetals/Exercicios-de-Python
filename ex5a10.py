#-*-coding:utf8;-*-
#qpy:console

n = int(input('Digite um número'))
a = n - 1
s = n + 1

print('O sucessor e o antecessor de {} é respectivamente {} e {}'.format(n,s,a))

n1 = int(input('Digite um número'))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print ('O dobro, o triplo e a raiz quadrada de {} é igual a {}, {} e {:.2}'.format(n1,d,t,r))

nota1 = float(input('Digite a nota'))
nota2 = float(input ('Digite a nota'))

m = (nota1+nota2)/2

print(m)
if m < 6:
    print('Reprovado')
else:
    print('Aprovado')

n2 = int(input('Digite um número'))

T = n2 * 0, n2 * 1, n2 * 2, n2 * 3, n2 * 4, n2 * 5, n2 * 6, n2 * 7, n2 * 8, n2 * 9

print('a tabuada de {} é igual a {}'.format(n2,T))

D = int(input('Digite seu saúdo'))
c = D / 3,27

print('Seu saúdo de dinheiro de Real, referente a R${}, \n para dólar é de U${}'.format(D,c))

