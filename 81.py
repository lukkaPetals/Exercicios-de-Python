from typing import Counter


lista = []
cont = 0
while True:
    v = int(input('Digite um valor: '))
    cont += 1
    print(f'O {cont}° valor foi digitado com sucesso')
    lista.append(v)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Foram {cont} valores digitados')
print(f'Os valores foram {lista}')
if 5 not in lista:
    print(f'O valor 5 não foi digitado e não está na lista')
else:
    print('O valor 5 está na lista')
