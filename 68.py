from random import randint
pc = randint(1, 5)
cont = 0
ligar = True

while ligar == True:
    print('Digite um número entre 1 e 5 e escolha impar ou par')
    ip = str(input('Ímpar ou Par? [I/P]: ')).upper()
    n = int(input('Digite um número entre 1 e 5: '))
    soma = pc + n
    v = (pc + n) % 2
    if (ip == 'I' and v != 0) or ip == 'P' and v == 0:
        print(f'Parábens, você venceu! O resultado foi de {soma}')
        cont += 1
    else:
        print(f'Você perdeu, o resultado foi de {soma}. Seu número de vitorias foi de {cont}')
        break
