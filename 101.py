def voto(a):
    from datetime import date
    ano = date.today().year
    idade =  ano - a
    if idade >= 16 and idade <= 18:
        print('Seu voto é opcional')
    elif idade < 16:
        print('Você não pode votar')
    else:
        print('Seu voto é obrigatorio')


a = int(input('Digite seu ano de nascimento: '))
voto(a)