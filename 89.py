from ast import Num

boletim = [[], [], [], []]
cont = 0

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1 + nota2) / 2
    boletim[0].append(nome)
    boletim[1].append(nota1)
    boletim[2].append(nota2)
    boletim[3].append(m)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'O boletim dos alunos foi: ')
for c in range(0, cont):
    print(f'{boletim[0][c]}...{boletim[3][c]}')
while True:
    confirmação = str(input('Você deseja ver as notas de algum aluno especifico? [S/N]: ').upper().strip())
    if confirmação == 'N':
        break
    for d in range(0, cont):
        print(f'ID:{d}...{boletim[0][d]}')
    quem = int(input('Digite o ID do aluno que deseja ver as notas: '))
    print(f'O/A Aluno(o) {boletim[0][quem]} teve as notas {boletim[1][quem]} e {boletim[2][quem]}')
    
