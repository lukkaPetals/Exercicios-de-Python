aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'A media de {aluno["Nome"]} foi: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'

print(f'O nome do aluno é {aluno["Nome"]}')
print(f'Sua média foi de {aluno["Média"]}')
print(f'A situação do Aluno é: {aluno["Situação"]}')
