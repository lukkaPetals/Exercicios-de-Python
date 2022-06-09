matriz = [[],[],[],[],[],[],[],[],[],[],[],[]]
soma = sum(matriz[11])
for c in range(1,10):
    n = int(input(f'Digite o {c}°: '))
    matriz[c].append(n)
    if n % 2 == 0:
        matriz[10].append(n)
    if c == 7 or 8 or 9:
        matriz[11].append(n)
print(f'{matriz[1]}{matriz[2]}{matriz[3]}')
print(f'{matriz[4]}{matriz[5]}{matriz[6]}')
print(f'{matriz[7]}{matriz[8]}{matriz[9]}')
print(f'A soma de todos os pares foi: {sum(matriz[10])}')
print(f'A soma dos valores da 3° coluna foi: {soma}')
'''print(f'O maior valor da 2° coluna foi: {}')'''
