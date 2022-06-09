jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas foram jogadas?: '))
for c in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols ele fez na partida {c+1}?: ')))
jogador['gols'] = gols
jogador['total de gols'] = sum(gols)
print('=' * 30)
for k, v in jogador.items():
    print(f'{k} está em {v}')
print('=' * 30)
