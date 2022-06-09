n = int(input('Digite um número: '))

for c in range(1, n + 1):
    if n % c == 0:
        print('{} não é primo'.format(n))
    else:
        print('{} é primo'.format(n))