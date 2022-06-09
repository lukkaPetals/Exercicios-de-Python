a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))

for c in range(1, 11):
    an = a1 + (c - 1) * r
    print(an)
