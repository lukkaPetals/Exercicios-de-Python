num = [[],[]]

for c in range(1, 8):
    v =(int(input(f'Digite o {c}° valor: ')))
    if v % 2 == 0:
        num[0].append(v)
    elif v % 2 != 0:
        num[1].append(v)
print(f'Os valores foram: {num}')
print(f'Os valores pares foram: {sorted(num[0])}')
print(f'Os valores impares foram: {sorted(num[1])}')
