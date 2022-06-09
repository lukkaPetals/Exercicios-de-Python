pessoa = {}
galera = []
mulheres = []
cont = 0
soma = 0

while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F/O(Outros)] ')).upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break 
media = soma / cont
print(f'Ao todo foram {cont} pessoas cadastradas')
print(f'A média de idade das pessoas foi de {media}')
print(f'As mulheres cadastradas foram: {mulheres}')
for i, p in enumerate(galera):
    if galera[i]['idade'] >= media:
        print(f'As pessoas com idade maior que a média são {p}')
