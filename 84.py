cont = 0
pessoas = []
peso = []
maior = menor = 0
while True:
    pessoas.append(str(input('Digite o nome de uma pessoa: ')))
    pessoas.append(float(input('Digite um peso: ')))
    print('Dados registrado')
    if len(peso) == 0:
        maior = menor = pessoas[0]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    pessoas.append(peso[:])
    peso.clear()
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(F'Os dados foram {pessoas}')
print(f'Foram {len(pessoas)} pessoas registradas')
print(f'A pessoa mais pesada teve {maior}KG')
print(f'A pessoa mais leve teve {menor}KG')
