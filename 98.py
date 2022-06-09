def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 (de 1 em 1)')
    for cont1 in range(1,11):
        print(f'{cont1}, ',end='')
    print('-=' * 20)
    print('Contagem de 10 até 0 (de 2 em 2)')
    for cont2 in range(10,-1,-2):
        print(f'{cont2}, ')
    print('-=' * 20)
    print('Contagem personalizada')
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    for cont3 in range(a, b+1, c):
        print(cont3)
    print('-=' * 20)


#Codigo Principal
contador()
