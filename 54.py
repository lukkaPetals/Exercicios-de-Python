from datetime import date
a = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    n = int(input('Digite o seu ano de nascimento'))
    i =  a - n
    if i >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo houveram {} pessoas maiores de idade'.format(totmaior))
print('Ao todo houveram {} pessoas menores de idade'.format(totmenor))
