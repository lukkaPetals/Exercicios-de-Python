maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}° pessoa'.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if c > maior:
            maior = p
        if c < menor:
            menor = p
print('O maior peso foi {}kg'.format(maior))
print('O menor peso foi {}kg'.format(menor))