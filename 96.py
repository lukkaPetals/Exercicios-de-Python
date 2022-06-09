def área(l, c):
    a = l * c
    print(f'A Área do terreno é: {a}')


print('Controle de terrenos')
print('-')
l = float(input('Largura (em metros):'))
c = float(input('Comprimento (em metros): '))
área(l, c)
