parar = False
cont1 = 0
cont2 = 0
maior = 0
menor = 0

while parar == False:
    n = int(input('Digite um número: '))
    cont1 += n
    cont2 += 1
    média = cont1 / cont2
    if cont2 == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    c = input('Deseja continuar?: [S/N] ').upper().strip()
    if c == 'N':
        parar = True
    print('A média é {}, o maior é {} e o menor {}'.format(média, maior, menor))