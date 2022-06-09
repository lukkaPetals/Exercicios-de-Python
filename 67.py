n = 0
cont = 0
while n >= 0:
    n = int(input('Digite o número para ser multiplicado: '))
    m = n * cont
    while cont != 10:
        cont += 1
        print(f' {n} X {cont} = {m}')
    if n < 0:
        break
