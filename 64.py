cont = 0
n = 0
num = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += n
    num += 1
print('O total de números digitados foi {} e a soma deles foi de {}'.format(num, cont))