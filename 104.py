def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            valor = int(valor)
            ok = True
        else:
            print('ERRO! DIGITE UM NÚMERO INTEIRO')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f"Você digitou {n}")
