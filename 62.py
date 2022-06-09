a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
cont = 1
t = 11
while cont != t:
    an = a1 + (cont - 1) * r
    cont += 1
    print(an)
    if cont == t:
        te = int(input('deseja ver mais quantos termos?'))
        t += te