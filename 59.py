E = False

while E == False:
    p = int(input('Digite o primeiro valor: '))
    s = int(input('Digite o segundo valor: '))
    m = int(input('Selecione 1 para ver a soma, 2 para subtrair, 3 para multiplicar e 4 para dividir: '))

    if m == 1:
        soma = p + s
        print('O resultado é {}'.format(soma))

    if m == 2:
        sub = p - s
        print('O resultado é {}'.format(sub))

    if m == 3:
        multi = p * s
        print('O resultado é {}'.format(multi))

    if m == 4:
        divi = p / s
        print('O resultado é {}'.format(divi))
    sair = str(input('Deseja sair? [S/N]: ')).upper()
    if sair == 'S':
        E = True
    if sair == 'N':
        print('Reinicando...')
