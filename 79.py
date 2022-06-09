l = []
while True:
    v = int(input('Digite um valor: '))
    if v not in l:
        l.append(v)
    else:
        print('Erro! Número já existente, tente novamente')
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
            break
r = sorted(l)
print(f'Os valores foram {r}')
