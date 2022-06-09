def ficha(n, g):
    if len(n) == 0 and len(g) == 0:
        print('O jogador desconhecido fez 0 gols')
    if len(n) == 0 and len(g) != 0:
        print(f'O jogador desconhecido fez {g} gol(s)')
    if len(n) != 0 and len(g) == 0:
        print(f'O jogador {n} fez 0 gols')
    if len(n) != 0 and len(g) != 0:
        print(f'O jogador {n} fez {g} gol(s)')

n = input('Digite o nome do jogador: ')
g = input('Digite o números de gols que ele fez: ')

ficha(n, g)
