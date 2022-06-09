contp = 0
cont1000 = 0
mbarato = 0
mcaro = 0
ncaro = ''
sair = 'S'
totp = 0

while sair == 'S':
    print('---ESTATISTICAS DE PRODUTOS---')
    contp += 1
    print(f'Produto numero {contp}')
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o preço do produto: R$'))
    totp += preço
    if preço > 1000:
        cont1000 += 1
    if preço < 0:
        mbarato = preço
    if preço > mcaro:
        mcaro = preço
        ncaro = nome
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()
print(f'O total dos preços é de {totp}')
print(f'Foram {cont1000} produtos com o valor superior a R$1000')
print(f'o produto mais caro é {ncaro}')
