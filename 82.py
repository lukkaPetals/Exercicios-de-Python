lista = []
listaP = []
listaI = []
while True:
    v = int(input('Digite um valor: '))
    print('A valor foi registrado')
    lista.append(v)
    if v % 2 == 0:
        listaP.append(v)
    elif v % 2 != 0:
        listaI.append(v)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(lista)
print(listaP)
print(listaI)
