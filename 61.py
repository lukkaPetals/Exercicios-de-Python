a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
cont = 1
while cont != 11:
    an = a1 + (cont - 1) * r
    cont += 1
    print(an)
