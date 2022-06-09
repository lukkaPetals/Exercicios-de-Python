l = []
for c in range(1, 6):
    l.append(int(input(f'Digite o {c}° valor: ')))
print(f'Os valores digitados foram {l}')
print(f'o menor valor foi {min(l)} e está na posição {l.index(min(l))}')
print(f'o maior valor foi {max(l)} e está na posição {l.index(max(l))}')
